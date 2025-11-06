#!/usr/bin/env python3
"""
Secure Wallet Manager - Find UTXOs using environment secrets
Uses seed phrase and master key from secure environment variables
"""

import os
import hashlib
import hmac
import base58
from utxo_scanner import UTXOScanner
import json
import time
from typing import List, Dict, Tuple

class SecureWalletManager:
    """Secure wallet that never exposes private keys"""
    
    def __init__(self):
        self.scanner = UTXOScanner()
        
        # Check if secrets are available
        self.has_seed = 'SEED_PHRASE' in os.environ
        self.has_master = 'MASTER_KEY' in os.environ
        
        if not (self.has_seed or self.has_master):
            raise ValueError("No wallet secrets found in environment")
            
        print("🔐 Secure wallet manager initialized")
        print(f"   📋 Seed phrase available: {self.has_seed}")
        print(f"   🔑 Master key available: {self.has_master}")
    
    def _get_seed_phrase(self) -> List[str]:
        """Get seed phrase from environment (never logged)"""
        if not self.has_seed:
            return None
        return os.environ['SEED_PHRASE'].strip().split()
    
    def _get_master_key(self) -> str:
        """Get master key from environment (never logged)"""
        if not self.has_master:
            return None
        return os.environ['MASTER_KEY'].strip()
    
    def derive_addresses_from_seed(self, num_addresses=20) -> List[Dict]:
        """Derive Bitcoin addresses from seed phrase"""
        if not self.has_seed:
            print("❌ No seed phrase available")
            return []
        
        print(f"🔑 Deriving {num_addresses} addresses from seed phrase...")
        
        # Get seed words securely 
        seed_words = self._get_seed_phrase()
        if len(seed_words) not in [12, 15, 18, 21, 24]:
            print(f"❌ Invalid seed phrase length: {len(seed_words)} words")
            return []
        
        print(f"   ✅ Valid {len(seed_words)}-word seed phrase detected")
        
        # For this demo, we'll generate deterministic addresses from seed hash
        # In production, use proper BIP32/39/44 derivation
        addresses = []
        
        # Create seed hash (without exposing actual seed)
        seed_string = ' '.join(seed_words)
        seed_hash = hashlib.sha256(seed_string.encode()).digest()
        
        # Derive addresses for different account types
        account_types = [
            {'name': 'Legacy (P2PKH)', 'prefix': '1', 'version': 0x00},
            {'name': 'SegWit (P2SH-P2WPKH)', 'prefix': '3', 'version': 0x05},
            {'name': 'Native SegWit (P2WPKH)', 'prefix': 'bc1q', 'version': None},
        ]
        
        for acc_type in account_types:
            for i in range(num_addresses // len(account_types)):
                # Generate deterministic key for this path
                path_data = f"m/44'/0'/0'/0/{i}".encode()
                derived_key = hmac.new(seed_hash, path_data, hashlib.sha256).digest()
                
                # Generate address based on account type
                if acc_type['prefix'] == '1':  # Legacy P2PKH
                    address = self._generate_p2pkh_address(derived_key)
                elif acc_type['prefix'] == '3':  # P2SH-P2WPKH  
                    address = self._generate_p2sh_address(derived_key)
                elif acc_type['prefix'] == 'bc1q':  # Native SegWit
                    address = self._generate_p2wpkh_address(derived_key)
                else:
                    continue
                    
                if address:
                    addresses.append({
                        'address': address,
                        'type': acc_type['name'],
                        'path': f"m/44'/0'/0'/0/{i}",
                        'index': i
                    })
        
        print(f"   ✅ Generated {len(addresses)} addresses")
        return addresses
    
    def _generate_p2pkh_address(self, private_key: bytes) -> str:
        """Generate Legacy P2PKH address"""
        try:
            # Simple deterministic address generation (demo purposes)
            # In production, use proper secp256k1 public key derivation
            pubkey_hash = hashlib.sha256(private_key).digest()[:20]
            
            # Add version byte (0x00 for mainnet P2PKH)
            versioned_payload = b'\x00' + pubkey_hash
            
            # Double SHA256 for checksum
            checksum = hashlib.sha256(hashlib.sha256(versioned_payload).digest()).digest()[:4]
            
            # Encode with Base58Check
            full_payload = versioned_payload + checksum
            return base58.b58encode(full_payload).decode()
            
        except Exception as e:
            print(f"   ❌ Error generating P2PKH address: {e}")
            return None
    
    def _generate_p2sh_address(self, private_key: bytes) -> str:
        """Generate P2SH-P2WPKH address"""
        try:
            # Generate P2SH address (simplified for demo)
            script_hash = hashlib.sha256(private_key).digest()[:20]
            
            # Add version byte (0x05 for mainnet P2SH)
            versioned_payload = b'\x05' + script_hash
            
            # Double SHA256 for checksum
            checksum = hashlib.sha256(hashlib.sha256(versioned_payload).digest()).digest()[:4]
            
            # Encode with Base58Check
            full_payload = versioned_payload + checksum
            return base58.b58encode(full_payload).decode()
            
        except Exception as e:
            print(f"   ❌ Error generating P2SH address: {e}")
            return None
    
    def _generate_p2wpkh_address(self, private_key: bytes) -> str:
        """Generate Native SegWit P2WPKH address"""
        try:
            # Generate bech32 address (simplified for demo)
            pubkey_hash = hashlib.sha256(private_key).digest()[:20]
            
            # Convert to bech32 (simplified - would need proper bech32 encoding)
            # For now, return a valid-looking bc1q address
            hex_hash = pubkey_hash.hex()
            return f"bc1q{hex_hash[:32]}"  # Truncated for demo
            
        except Exception as e:
            print(f"   ❌ Error generating P2WPKH address: {e}")
            return None
    
    def scan_wallet_utxos(self, max_addresses=60, min_value_btc=0.001) -> List[Dict]:
        """Scan wallet for UTXOs"""
        print("💰 SECURE WALLET UTXO SCAN")
        print("=" * 50)
        
        # Derive addresses from seed
        addresses = self.derive_addresses_from_seed(max_addresses)
        
        if not addresses:
            print("❌ Could not derive addresses from wallet")
            return []
        
        # Extract address strings for scanning
        address_list = [addr['address'] for addr in addresses if addr['address']]
        
        print(f"🔍 Scanning {len(address_list)} derived addresses...")
        
        # Scan for UTXOs
        utxos = self.scanner.find_large_utxos(
            address_list,
            min_value_btc=min_value_btc,
            min_confirmations=1
        )
        
        if utxos:
            # Add wallet metadata
            for utxo in utxos:
                # Find which derived address this UTXO belongs to
                for addr_info in addresses:
                    if addr_info['address'] == utxo['address']:
                        utxo['wallet_type'] = addr_info['type']
                        utxo['derivation_path'] = addr_info['path']
                        utxo['address_index'] = addr_info['index']
                        break
            
            print(f"\n" + self.scanner.generate_utxo_summary(utxos))
            
            # Save secure summary (no private keys)
            summary = {
                'timestamp': time.time(),
                'total_addresses_scanned': len(address_list),
                'utxos_found': len(utxos),
                'total_value_btc': sum(utxo['value'] for utxo in utxos) / 100000000,
                'largest_utxos': utxos[:10]  # Top 10
            }
            
            with open('wallet_utxos_secure.json', 'w') as f:
                json.dump(summary, f, indent=2)
                
            print(f"\n✅ Saved secure UTXO summary to wallet_utxos_secure.json")
            
        return utxos
    
    def find_transaction_ready_utxos(self, target_btc=10.0) -> Dict:
        """Find UTXOs ready for large transactions"""
        print(f"🎯 FINDING UTXOs FOR {target_btc} BTC TRANSACTION")
        print("=" * 60)
        
        utxos = self.scan_wallet_utxos(max_addresses=100, min_value_btc=0.1)
        
        if not utxos:
            return {'ready': False, 'message': 'No UTXOs found in wallet'}
        
        # Sort by value (largest first)
        utxos.sort(key=lambda x: x['value'], reverse=True)
        
        target_sats = int(target_btc * 100000000)
        total_value = 0
        selected_utxos = []
        
        print(f"\n🎯 SELECTING UTXOs FOR {target_btc} BTC TARGET:")
        print("=" * 50)
        
        for utxo in utxos:
            selected_utxos.append(utxo)
            total_value += utxo['value']
            
            btc_value = utxo['value'] / 100000000
            print(f"   ✅ Selected: {btc_value:12.8f} BTC ({utxo['wallet_type']})")
            print(f"      TXID: {utxo['txid']}")
            print(f"      VOUT: {utxo['vout']}")
            print(f"      Path: {utxo['derivation_path']}")
            print()
            
            if total_value >= target_sats:
                break
                
            if len(selected_utxos) >= 10:  # Max 10 inputs
                break
        
        total_btc = total_value / 100000000
        
        if total_value >= target_sats:
            print(f"🎉 SUCCESS! Selected {total_btc:.8f} BTC from {len(selected_utxos)} UTXOs")
            
            result = {
                'ready': True,
                'total_value_btc': total_btc,
                'total_value_sats': total_value,
                'utxo_count': len(selected_utxos),
                'selected_utxos': selected_utxos,
                'change_amount_btc': total_btc - target_btc
            }
            
            # Save transaction-ready UTXOs
            with open('transaction_ready_utxos.json', 'w') as f:
                json.dump(result, f, indent=2)
                
            print(f"💾 Saved transaction inputs to transaction_ready_utxos.json")
            return result
            
        else:
            print(f"❌ INSUFFICIENT FUNDS: Only {total_btc:.8f} BTC available")
            return {
                'ready': False,
                'message': f'Insufficient funds: {total_btc:.8f} BTC < {target_btc} BTC target',
                'available_btc': total_btc,
                'shortfall_btc': target_btc - total_btc
            }

def main():
    """Main function to find wallet UTXOs"""
    try:
        wallet = SecureWalletManager()
        
        # Find UTXOs for large transaction (adjust target as needed)
        result = wallet.find_transaction_ready_utxos(target_btc=9.5)  # 9.5 BTC target
        
        if result['ready']:
            print(f"\n🚀 WALLET READY FOR TRANSACTION!")
            print(f"   💰 Available: {result['total_value_btc']:.8f} BTC")
            print(f"   🎯 Change: {result['change_amount_btc']:.8f} BTC")
            print(f"   📊 Inputs: {result['utxo_count']} UTXOs")
        else:
            print(f"\n⚠️  WALLET NOT READY: {result['message']}")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()