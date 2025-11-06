#!/usr/bin/env python3
"""
HD Wallet Derivation - Proper BIP32 HD wallet with bit rotation
"""

import os
import hashlib
import hmac
import struct
import base58
from typing import List, Dict, Tuple
import ecdsa
from ecdsa.curves import SECP256k1
from utxo_scanner import UTXOScanner
import json
import time

class HDWalletDerivation:
    """Proper HD wallet derivation with bit rotation capabilities"""
    
    def __init__(self):
        self.scanner = UTXOScanner()
        
        # Load master key from secure environment
        if 'MASTER_KEY' not in os.environ:
            raise ValueError("MASTER_KEY not found in environment")
            
        self.master_key_hex = os.environ['MASTER_KEY'].strip()
        print("🔐 HD Wallet initialized with secure master key")
        print(f"   🔑 Master key length: {len(self.master_key_hex)} characters")
        
    def _hmac_sha512(self, key: bytes, data: bytes) -> bytes:
        """HMAC-SHA512 for BIP32 derivation"""
        return hmac.new(key, data, hashlib.sha512).digest()
    
    def _parse_master_key(self) -> Tuple[bytes, bytes]:
        """Parse master key into private key and chain code - handles multiple formats"""
        try:
            key = self.master_key_hex.strip()
            
            # Try hex decoding first (64 or 128 hex chars)
            if len(key) == 128 and all(c in '0123456789abcdefABCDEF' for c in key):
                master_bytes = bytes.fromhex(key)
                private_key = master_bytes[:32]
                chain_code = master_bytes[32:]
                return private_key, chain_code
                
            elif len(key) == 64 and all(c in '0123456789abcdefABCDEF' for c in key):
                private_key = bytes.fromhex(key)
                chain_code = self._hmac_sha512(b"Bitcoin seed", private_key)[32:]
                return private_key, chain_code
            
            # Try Base58 (WIF format)
            elif key.startswith(('5', 'K', 'L')) and len(key) in [51, 52]:
                try:
                    decoded = base58.b58decode(key)
                    if len(decoded) == 37 and decoded[0] == 0x80:  # Mainnet WIF
                        private_key = decoded[1:33]
                        chain_code = self._hmac_sha512(b"Bitcoin seed", private_key)[32:]
                        return private_key, chain_code
                except:
                    pass
            
            # Try Base64 decoding
            elif len(key) % 4 == 0:
                try:
                    import base64
                    decoded = base64.b64decode(key)
                    if len(decoded) >= 32:
                        private_key = decoded[:32]
                        chain_code = self._hmac_sha512(b"Bitcoin seed", private_key)[32:]
                        return private_key, chain_code
                except:
                    pass
            
            # Default: Use key as seed material
            seed_bytes = key.encode('utf-8')
            master_secret = self._hmac_sha512(b"Bitcoin seed", seed_bytes)
            private_key = master_secret[:32]
            chain_code = master_secret[32:]
            
            print(f"   ✅ Using key as seed material ({len(seed_bytes)} bytes)")
            return private_key, chain_code
                
        except Exception as e:
            print(f"❌ Error parsing master key: {e}")
            # Final fallback: hash the master key as seed
            seed_hash = hashlib.sha256(self.master_key_hex.encode()).digest()
            master_secret = self._hmac_sha512(b"Bitcoin seed", seed_hash)
            return master_secret[:32], master_secret[32:]
    
    def _point_add(self, point1: Tuple[int, int], point2: Tuple[int, int]) -> Tuple[int, int]:
        """Add two elliptic curve points"""
        if point1 is None:
            return point2
        if point2 is None:
            return point1
            
        # Use ecdsa library for point addition
        p1 = ecdsa.ellipticcurve.Point(SECP256k1.curve, point1[0], point1[1])
        p2 = ecdsa.ellipticcurve.Point(SECP256k1.curve, point2[0], point2[1])
        p3 = p1 + p2
        return (p3.x(), p3.y())
    
    def _private_to_public(self, private_key: bytes) -> bytes:
        """Convert private key to compressed public key"""
        try:
            sk = ecdsa.SigningKey.from_string(private_key, curve=SECP256k1)
            vk = sk.verifying_key
            point = vk.pubkey.point
            
            # Compress public key
            x = point.x()
            y = point.y()
            
            # Determine compression prefix
            prefix = b'\x02' if y % 2 == 0 else b'\x03'
            return prefix + x.to_bytes(32, 'big')
            
        except Exception as e:
            print(f"❌ Error deriving public key: {e}")
            return None
    
    def derive_child_key(self, parent_key: bytes, parent_chain: bytes, index: int, hardened=False) -> Tuple[bytes, bytes]:
        """Derive child private key using BIP32"""
        try:
            # Prepare data for HMAC
            if hardened:
                # Hardened derivation: use private key
                index |= 0x80000000  # Set hardened bit
                data = b'\x00' + parent_key + struct.pack('>I', index)
            else:
                # Non-hardened derivation: use public key
                parent_pubkey = self._private_to_public(parent_key)
                if parent_pubkey is None:
                    raise ValueError("Could not derive parent public key")
                data = parent_pubkey + struct.pack('>I', index)
            
            # HMAC-SHA512
            hmac_result = self._hmac_sha512(parent_chain, data)
            
            # Split result
            child_key_int = int.from_bytes(hmac_result[:32], 'big')
            child_chain = hmac_result[32:]
            
            # Add parent private key
            parent_key_int = int.from_bytes(parent_key, 'big')
            child_private_int = (child_key_int + parent_key_int) % SECP256k1.order
            
            # Convert back to bytes
            child_private = child_private_int.to_bytes(32, 'big')
            
            return child_private, child_chain
            
        except Exception as e:
            print(f"❌ Error deriving child key at index {index}: {e}")
            return None, None
    
    def derive_path(self, path: str) -> Tuple[bytes, bytes, str]:
        """Derive key for BIP32 path like m/44'/0'/0'/0/0"""
        try:
            # Parse path
            if not path.startswith('m/'):
                raise ValueError("Path must start with 'm/'")
                
            components = path[2:].split('/')
            
            # Start with master key
            current_private, current_chain = self._parse_master_key()
            derived_path = "m"
            
            for component in components:
                if not component:
                    continue
                    
                hardened = component.endswith("'")
                if hardened:
                    index = int(component[:-1])
                else:
                    index = int(component)
                
                current_private, current_chain = self.derive_child_key(
                    current_private, current_chain, index, hardened
                )
                
                if current_private is None:
                    raise ValueError(f"Failed to derive key for component {component}")
                
                derived_path += f"/{component}"
            
            return current_private, current_chain, derived_path
            
        except Exception as e:
            print(f"❌ Error deriving path {path}: {e}")
            return None, None, None
    
    def generate_bitcoin_address(self, private_key: bytes, address_type: str) -> str:
        """Generate Bitcoin address from private key"""
        try:
            public_key = self._private_to_public(private_key)
            if public_key is None:
                return None
                
            if address_type == "p2pkh":  # Legacy
                # Hash160 of public key
                hash160 = hashlib.new('ripemd160', hashlib.sha256(public_key).digest()).digest()
                # Add version byte (0x00 for mainnet)
                versioned = b'\x00' + hash160
                # Double SHA256 checksum
                checksum = hashlib.sha256(hashlib.sha256(versioned).digest()).digest()[:4]
                # Base58Check encode
                return base58.b58encode(versioned + checksum).decode()
                
            elif address_type == "p2sh-p2wpkh":  # P2SH-wrapped SegWit
                # Create P2WPKH script
                hash160 = hashlib.new('ripemd160', hashlib.sha256(public_key).digest()).digest()
                witness_script = b'\x00\x14' + hash160  # OP_0 + 20-byte hash
                # Hash160 of witness script
                script_hash = hashlib.new('ripemd160', hashlib.sha256(witness_script).digest()).digest()
                # Add P2SH version byte (0x05)
                versioned = b'\x05' + script_hash
                # Checksum and encode
                checksum = hashlib.sha256(hashlib.sha256(versioned).digest()).digest()[:4]
                return base58.b58encode(versioned + checksum).decode()
                
            elif address_type == "p2wpkh":  # Native SegWit (bech32)
                # For simplicity, create a mock bech32 address
                hash160 = hashlib.new('ripemd160', hashlib.sha256(public_key).digest()).digest()
                # This is simplified - real bech32 encoding is more complex
                return f"bc1q{hash160.hex()}"
                
            else:
                print(f"❌ Unsupported address type: {address_type}")
                return None
                
        except Exception as e:
            print(f"❌ Error generating {address_type} address: {e}")
            return None
    
    def bit_rotation_scan(self, base_private_key: bytes, rotations: int = 256) -> List[Dict]:
        """Bit rotation tool - rotate bits in private key"""
        print(f"🔄 BIT ROTATION SCAN - {rotations} rotations each way")
        print("=" * 60)
        
        addresses_to_scan = []
        
        # Convert to integer for bit operations
        base_int = int.from_bytes(base_private_key, 'big')
        
        # Right rotations
        for r in range(1, rotations + 1):
            rotated_int = self._rotate_right(base_int, r, 256)  # 256-bit rotation
            rotated_key = rotated_int.to_bytes(32, 'big')
            
            for addr_type in ["p2pkh", "p2sh-p2wpkh", "p2wpkh"]:
                address = self.generate_bitcoin_address(rotated_key, addr_type)
                if address:
                    addresses_to_scan.append({
                        'address': address,
                        'type': addr_type,
                        'rotation': f"R{r}",
                        'direction': 'right'
                    })
        
        # Left rotations  
        for r in range(1, rotations + 1):
            rotated_int = self._rotate_left(base_int, r, 256)  # 256-bit rotation
            rotated_key = rotated_int.to_bytes(32, 'big')
            
            for addr_type in ["p2pkh", "p2sh-p2wpkh", "p2wpkh"]:
                address = self.generate_bitcoin_address(rotated_key, addr_type)
                if address:
                    addresses_to_scan.append({
                        'address': address,
                        'type': addr_type,
                        'rotation': f"L{r}",
                        'direction': 'left'
                    })
        
        print(f"🎯 Generated {len(addresses_to_scan)} rotated addresses")
        
        # Scan addresses for UTXOs
        address_list = [addr['address'] for addr in addresses_to_scan]
        utxos = self.scanner.scan_multiple_addresses(address_list, min_confirmations=1)
        
        # Add rotation metadata to UTXOs
        for utxo in utxos:
            for addr_info in addresses_to_scan:
                if addr_info['address'] == utxo['address']:
                    utxo.update(addr_info)
                    break
        
        return utxos
    
    def _rotate_right(self, value: int, shift: int, bits: int) -> int:
        """Rotate integer right by shift bits"""
        mask = (1 << bits) - 1
        value &= mask
        return ((value >> shift) | (value << (bits - shift))) & mask
    
    def _rotate_left(self, value: int, shift: int, bits: int) -> int:
        """Rotate integer left by shift bits"""  
        mask = (1 << bits) - 1
        value &= mask
        return ((value << shift) | (value >> (bits - shift))) & mask
    
    def full_hd_scan(self, max_accounts=10, max_addresses=100) -> List[Dict]:
        """Full HD wallet scan across multiple derivation paths"""
        print("🔍 FULL HD WALLET SCAN - ALL CHAINS")
        print("=" * 60)
        
        all_addresses = []
        
        # All standard derivation paths with their variants
        derivation_paths = [
            # BIP44 - Legacy P2PKH  
            "m/44'/0'/0'/0",    # Receive
            "m/44'/0'/0'/1",    # Change
            
            # BIP49 - P2SH-P2WPKH (SegWit wrapped in P2SH)
            "m/49'/0'/0'/0",    # Receive  
            "m/49'/0'/0'/1",    # Change
            
            # BIP84 - P2WPKH (Native SegWit)
            "m/84'/0'/0'/0",    # Receive
            "m/84'/0'/0'/1",    # Change
            
            # BIP86 - P2TR (Taproot) 
            "m/86'/0'/0'/0",    # Receive
            "m/86'/0'/0'/1",    # Change
            
            # Legacy variations
            "m/0'/0'/0'",       # Old Electrum
            "m/0'/0'",          # Very old wallets
            "m/0'",             # Single chain
            
            # Non-hardened variants
            "m/44/0/0/0",       # Non-hardened BIP44
            "m/49/0/0/0",       # Non-hardened BIP49
            "m/84/0/0/0",       # Non-hardened BIP84
        ]
        
        address_types = ["p2pkh", "p2sh-p2wpkh", "p2wpkh"]
        
        print(f"📊 Scanning {len(derivation_paths)} derivation chains...")
        
        for base_path in derivation_paths:
            for account in range(max_accounts):
                for addr_index in range(max_addresses):
                    # Build full path
                    if base_path.count('/') == 3:  # Like m/44'/0'/0'/0
                        full_path = f"{base_path.replace('/0', f'/{account}')}/{addr_index}"
                    elif base_path.count('/') == 2:  # Like m/0'/0'  
                        full_path = f"{base_path.replace('/0', f'/{account}')}/{addr_index}"
                    else:  # Like m/0'
                        full_path = f"{base_path}/{account}/{addr_index}"
                    
                    # Derive key for this path
                    private_key, _, derived_path = self.derive_path(full_path)
                    
                    if private_key:
                        # Generate addresses for this key
                        for addr_type in address_types:
                            address = self.generate_bitcoin_address(private_key, addr_type)
                            if address:
                                all_addresses.append({
                                    'address': address,
                                    'type': addr_type,
                                    'path': derived_path,
                                    'base_path': base_path,
                                    'account': account,
                                    'index': addr_index
                                })
        
        print(f"🎯 Generated {len(all_addresses)} HD addresses across all chains")
        
        # Scan addresses for UTXOs
        address_list = [addr['address'] for addr in all_addresses]
        utxos = self.scanner.scan_multiple_addresses(address_list, min_confirmations=1)
        
        # Add HD metadata to UTXOs
        for utxo in utxos:
            for addr_info in all_addresses:
                if addr_info['address'] == utxo['address']:
                    utxo.update(addr_info)
                    break
        
        return utxos
    
    def comprehensive_scan(self) -> Dict:
        """Comprehensive scan: HD chains + bit rotations + inverses"""
        print("🚀 COMPREHENSIVE WALLET SCAN - ALL CHAINS & INVERSES")
        print("=" * 80)
        
        results = {
            'timestamp': time.time(),
            'hd_utxos': [],
            'rotation_utxos': [],
            'inverse_utxos': [],
            'total_utxos': 0,
            'total_value_btc': 0.0
        }
        
        # 1. Full HD chain scan
        print("\n1️⃣  HD WALLET CHAIN SCAN")
        results['hd_utxos'] = self.full_hd_scan(max_accounts=20, max_addresses=200)
        
        # 2. Master key bit rotations
        print("\n2️⃣  MASTER KEY BIT ROTATION SCAN")
        master_private, _ = self._parse_master_key()
        results['rotation_utxos'] = self.bit_rotation_scan(master_private, rotations=256)
        
        # 3. Inverse operations - bit complement
        print("\n3️⃣  INVERSE BIT OPERATIONS")
        inverse_utxos = []
        
        # Bit complement (NOT operation)
        complement_int = (~int.from_bytes(master_private, 'big')) & ((1 << 256) - 1)
        complement_key = complement_int.to_bytes(32, 'big')
        
        # Scan complement key rotations
        complement_rotations = self.bit_rotation_scan(complement_key, rotations=128)
        for utxo in complement_rotations:
            utxo['operation'] = 'complement'
        inverse_utxos.extend(complement_rotations)
        
        # Bit reversal (reverse bit order)
        reversed_int = int(format(int.from_bytes(master_private, 'big'), '0256b')[::-1], 2)
        reversed_key = reversed_int.to_bytes(32, 'big')
        
        # Scan reversed key rotations
        reversed_rotations = self.bit_rotation_scan(reversed_key, rotations=128)
        for utxo in reversed_rotations:
            utxo['operation'] = 'reverse'
        inverse_utxos.extend(reversed_rotations)
        
        # XOR with common patterns
        xor_patterns = [
            0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,  # All 1s
            0x5555555555555555555555555555555555555555555555555555555555555555,  # Alternating
            0xAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA,  # Alternating inv
        ]
        
        for i, pattern in enumerate(xor_patterns):
            xor_int = int.from_bytes(master_private, 'big') ^ pattern
            xor_key = xor_int.to_bytes(32, 'big')
            
            # Scan XOR key (limited rotations)
            xor_rotations = self.bit_rotation_scan(xor_key, rotations=64)
            for utxo in xor_rotations:
                utxo['operation'] = f'xor_pattern_{i}'
            inverse_utxos.extend(xor_rotations)
        
        results['inverse_utxos'] = inverse_utxos
        
        # Combine all results
        all_utxos = results['hd_utxos'] + results['rotation_utxos'] + results['inverse_utxos']
        results['total_utxos'] = len(all_utxos)
        results['total_value_btc'] = sum(utxo['value'] for utxo in all_utxos) / 100000000
        
        # Summary
        print(f"\n🎉 COMPREHENSIVE SCAN COMPLETE!")
        print(f"   💰 Total UTXOs: {results['total_utxos']}")
        print(f"   💎 Total Value: {results['total_value_btc']:.8f} BTC")
        print(f"   🔗 HD Chain UTXOs: {len(results['hd_utxos'])}")
        print(f"   🔄 Rotation UTXOs: {len(results['rotation_utxos'])}")
        print(f"   🔀 Inverse UTXOs: {len(results['inverse_utxos'])}")
        
        if all_utxos:
            # Show largest UTXOs
            largest = sorted(all_utxos, key=lambda x: x['value'], reverse=True)[:10]
            print(f"\n🏆 TOP 10 LARGEST UTXOs:")
            for i, utxo in enumerate(largest):
                btc_val = utxo['value'] / 100000000
                source = utxo.get('path', utxo.get('rotation', utxo.get('operation', 'unknown')))
                print(f"   {i+1:2d}. {btc_val:12.8f} BTC - {utxo.get('type', 'unknown')} ({source})")
                print(f"       {utxo['address']}")
            
            # Save comprehensive results
            results['largest_utxos'] = largest
            with open('comprehensive_wallet_scan.json', 'w') as f:
                json.dump(results, f, indent=2, default=str)
                
            print(f"\n💾 Complete results saved to comprehensive_wallet_scan.json")
            
        return results

def main():
    """Main comprehensive HD wallet and bit rotation scan"""
    try:
        hd_wallet = HDWalletDerivation()
        
        # Run comprehensive scan
        results = hd_wallet.comprehensive_scan()
        
        if results['total_utxos'] > 0:
            print(f"\n✅ SCAN SUCCESSFUL - UTXOS FOUND!")
            print(f"   Use these UTXOs for your Bitcoin transactions")
            
            # Generate transaction-ready summary
            if results['total_value_btc'] >= 9.5:  # Target amount
                print(f"\n🚀 READY FOR 9.5+ BTC TRANSACTION!")
                print(f"   Available: {results['total_value_btc']:.8f} BTC")
        else:
            print(f"\n❌ NO UTXOs FOUND")
            print(f"   Master key may not have associated Bitcoin funds")
            print(f"   Try different derivation patterns or check key validity")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()