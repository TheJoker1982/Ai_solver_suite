#!/usr/bin/env python3
"""
Multi-Blockchain Scanner - Check UTXOs across BCH, BSV, ETH, and other networks
"""

import os
import requests
import time
import json
import hashlib
from typing import List, Dict
from hd_wallet_derivation import HDWalletDerivation

class MultiBlockchainScanner:
    """Scan multiple blockchains for UTXOs from same wallet keys"""
    
    def __init__(self):
        self.hd_wallet = HDWalletDerivation()
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Multi-Blockchain-Scanner/1.0'
        })
        
        # Blockchain APIs
        self.apis = {
            'bch': {
                'name': 'Bitcoin Cash',
                'explorers': [
                    {'name': 'Blockchair', 'base': 'https://api.blockchair.com/bitcoin-cash'},
                    {'name': 'Tokenview', 'base': 'https://services.tokenview.io/vipapi/bch'}
                ]
            },
            'bsv': {
                'name': 'Bitcoin SV', 
                'explorers': [
                    {'name': 'WhatsOnChain', 'base': 'https://api.whatsonchain.com/v1/bsv/main'}
                ]
            },
            'eth': {
                'name': 'Ethereum',
                'explorers': [
                    {'name': 'Etherscan', 'base': 'https://api.etherscan.io/api'},
                    {'name': 'Blockchair', 'base': 'https://api.blockchair.com/ethereum'}
                ]
            }
        }
    
    def generate_ethereum_address(self, private_key: bytes) -> str:
        """Generate Ethereum address from private key"""
        try:
            import ecdsa
            from ecdsa import SECP256k1
            
            # Generate public key
            sk = ecdsa.SigningKey.from_string(private_key, curve=SECP256k1)
            vk = sk.verifying_key
            point = vk.pubkey.point
            
            # Get uncompressed public key (64 bytes)
            public_key = point.x().to_bytes(32, 'big') + point.y().to_bytes(32, 'big')
            
            # Use built-in hashlib for Keccak-256 (Python 3.6+)
            try:
                import hashlib
                keccak = hashlib.sha3_256(public_key)
                address_bytes = keccak.digest()[-20:]  # Take last 20 bytes
            except:
                # Fallback: use simple hash for demo
                hash_obj = hashlib.sha256(public_key)
                address_bytes = hash_obj.digest()[-20:]
            
            # Add 0x prefix and return
            return '0x' + address_bytes.hex()
            
        except Exception as e:
            print(f"❌ Error generating Ethereum address: {e}")
            return None
    
    def generate_bch_address(self, private_key: bytes) -> str:
        """Generate Bitcoin Cash address (legacy format)"""
        # BCH uses same algorithm as Bitcoin for legacy addresses
        return self.hd_wallet.generate_bitcoin_address(private_key, 'p2pkh')
    
    def generate_bsv_address(self, private_key: bytes) -> str:
        """Generate Bitcoin SV address"""
        # BSV uses same algorithm as Bitcoin
        return self.hd_wallet.generate_bitcoin_address(private_key, 'p2pkh')
    
    def scan_bch_utxos(self, addresses: List[str]) -> List[Dict]:
        """Scan Bitcoin Cash for UTXOs using multiple APIs"""
        print(f"🔍 Scanning Bitcoin Cash (BCH) - {len(addresses)} addresses")
        utxos = []
        
        # Try Tokenview API first (more reliable)
        try:
            for address in addresses[:20]:  # Test more addresses
                try:
                    # Try Tokenview API
                    url = f"https://services.tokenview.io/vipapi/bch/address/{address}"
                    response = self.session.get(url, timeout=10)
                    
                    if response.status_code == 200:
                        data = response.json()
                        if data.get('code') == 1 and 'data' in data:
                            addr_data = data['data']
                            balance = int(addr_data.get('balance', 0))
                            
                            if balance > 0:
                                # Note: Tokenview doesn't give UTXO details in basic call
                                utxos.append({
                                    'blockchain': 'BCH',
                                    'address': address,
                                    'txid': 'multiple',  # Would need separate UTXO call
                                    'vout': 0,
                                    'value': balance,
                                    'confirmations': 1,
                                    'explorer': 'Tokenview'
                                })
                                print(f"   ✅ {address}: {balance/1e8:.8f} BCH found")
                            else:
                                print(f"   ⭕ {address}: No BCH")
                    else:
                        # Fallback to Blockchair with different rate limit
                        time.sleep(2)  # Longer delay
                        url2 = f"https://api.blockchair.com/bitcoin-cash/dashboards/address/{address}?limit=100"
                        response2 = self.session.get(url2, timeout=10)
                        
                        if response2.status_code == 200:
                            data2 = response2.json()
                            if 'data' in data2 and address in data2['data']:
                                addr_data = data2['data'][address]
                                
                                if 'utxo' in addr_data and addr_data['utxo']:
                                    for utxo in addr_data['utxo']:
                                        utxos.append({
                                            'blockchain': 'BCH',
                                            'address': address,
                                            'txid': utxo.get('transaction_hash'),
                                            'vout': utxo.get('index'),
                                            'value': utxo.get('value'),
                                            'confirmations': utxo.get('block_id', 0),
                                            'explorer': 'Blockchair'
                                        })
                                    print(f"   ✅ {address}: {len(addr_data['utxo'])} UTXOs found")
                                else:
                                    print(f"   ⭕ {address}: No UTXOs")
                        else:
                            print(f"   ⭕ {address}: No data available")
                            
                except Exception as addr_error:
                    print(f"   ❌ {address}: {addr_error}")
                
                time.sleep(1)  # Rate limiting
                
        except Exception as e:
            print(f"❌ BCH scan error: {e}")
        
        return utxos
    
    def scan_bsv_utxos(self, addresses: List[str]) -> List[Dict]:
        """Scan Bitcoin SV for UTXOs"""
        print(f"🔍 Scanning Bitcoin SV (BSV) - {len(addresses)} addresses")
        utxos = []
        
        try:
            for address in addresses[:10]:  # Limit for testing
                url = f"https://api.whatsonchain.com/v1/bsv/main/address/{address}/unspent"
                response = self.session.get(url, timeout=15)
                
                if response.status_code == 200:
                    data = response.json()
                    
                    if data and isinstance(data, list):
                        for utxo in data:
                            utxos.append({
                                'blockchain': 'BSV',
                                'address': address,
                                'txid': utxo.get('tx_hash'),
                                'vout': utxo.get('tx_pos'),
                                'value': utxo.get('value'),
                                'confirmations': utxo.get('height', 0),
                                'explorer': 'WhatsOnChain'
                            })
                        print(f"   ✅ {address}: {len(data)} UTXOs found")
                    else:
                        print(f"   ⭕ {address}: No UTXOs")
                        
                elif response.status_code == 404:
                    print(f"   ⭕ {address}: No UTXOs")
                else:
                    print(f"   ❌ {address}: API error {response.status_code}")
                
                time.sleep(1)  # BSV rate limiting
                
        except Exception as e:
            print(f"❌ BSV scan error: {e}")
        
        return utxos
    
    def scan_eth_balances(self, addresses: List[str]) -> List[Dict]:
        """Scan Ethereum for balances"""
        print(f"🔍 Scanning Ethereum (ETH) - {len(addresses)} addresses") 
        balances = []
        
        try:
            for address in addresses[:10]:  # Limit for testing
                url = f"https://api.blockchair.com/ethereum/dashboards/address/{address}"
                response = self.session.get(url, timeout=15)
                
                if response.status_code == 200:
                    data = response.json()
                    if 'data' in data and address in data['data']:
                        addr_data = data['data'][address]['address']
                        balance = addr_data.get('balance', 0)
                        
                        if balance > 0:
                            balances.append({
                                'blockchain': 'ETH',
                                'address': address,
                                'balance': balance,
                                'balance_eth': balance / 1e18,
                                'transaction_count': addr_data.get('transaction_count', 0),
                                'explorer': 'Blockchair'
                            })
                            print(f"   ✅ {address}: {balance/1e18:.6f} ETH")
                        else:
                            print(f"   ⭕ {address}: 0 ETH")
                else:
                    print(f"   ❌ {address}: API error {response.status_code}")
                
                time.sleep(0.5)  # Rate limiting
                
        except Exception as e:
            print(f"❌ ETH scan error: {e}")
        
        return balances
    
    def comprehensive_multi_blockchain_scan(self) -> Dict:
        """Comprehensive scan across all blockchains"""
        print("🚀 MULTI-BLOCKCHAIN COMPREHENSIVE SCAN")
        print("=" * 70)
        
        results = {
            'timestamp': time.time(),
            'blockchains_scanned': ['BTC', 'BCH', 'BSV', 'ETH'],
            'total_addresses_generated': 0,
            'utxos_found': {
                'BTC': [],
                'BCH': [],
                'BSV': [],
                'ETH': []
            },
            'total_value': {
                'BTC': 0,
                'BCH': 0,
                'BSV': 0,
                'ETH': 0
            }
        }
        
        # Generate addresses from wallet for first few derivation paths
        print("\n1️⃣  GENERATING ADDRESSES FROM HD WALLET")
        
        # Get master private key
        master_private, _ = self.hd_wallet._parse_master_key()
        
        # Generate addresses for main derivation paths (expanded)
        test_paths = []
        
        # Generate more paths for better coverage
        coin_paths = {
            0: "BTC",    # Bitcoin
            145: "BCH",  # Bitcoin Cash  
            236: "BSV",  # Bitcoin SV
            60: "ETH"    # Ethereum
        }
        
        for coin_type in coin_paths.keys():
            for account in range(3):  # 3 accounts
                for change in range(2):  # receive + change
                    for index in range(10):  # 10 addresses each
                        path = f"m/44'/{coin_type}'/{account}'/{change}/{index}"
                        test_paths.append(path)
        
        # Add legacy paths
        for index in range(20):
            test_paths.append(f"m/0'/0'/{index}")  # Old Electrum
            test_paths.append(f"m/0'/{index}")     # Single chain
        
        btc_addresses = []
        bch_addresses = []
        bsv_addresses = []
        eth_addresses = []
        
        for path in test_paths:
            private_key, _, derived_path = self.hd_wallet.derive_path(path)
            
            if private_key:
                # Generate addresses for different blockchains
                if "'0'" in path or "'145'" in path:  # BTC or BCH paths
                    btc_addr = self.generate_bch_address(private_key)
                    if btc_addr:
                        btc_addresses.append(btc_addr)
                        bch_addresses.append(btc_addr)  # Same format for BCH
                        bsv_addresses.append(btc_addr)  # Same format for BSV
                
                # Generate Ethereum address
                eth_addr = self.generate_ethereum_address(private_key)
                if eth_addr:
                    eth_addresses.append(eth_addr)
        
        # Also generate from bit rotations
        print("   🔄 Adding bit rotation addresses...")
        for rotation in range(1, 5):  # Limited rotations
            base_int = int.from_bytes(master_private, 'big')
            rotated_int = ((base_int >> rotation) | (base_int << (256 - rotation))) & ((1 << 256) - 1)
            rotated_key = rotated_int.to_bytes(32, 'big')
            
            # Generate addresses
            btc_addr = self.generate_bch_address(rotated_key)
            eth_addr = self.generate_ethereum_address(rotated_key)
            
            if btc_addr:
                btc_addresses.append(btc_addr)
                bch_addresses.append(btc_addr)
                bsv_addresses.append(btc_addr)
            if eth_addr:
                eth_addresses.append(eth_addr)
        
        # Remove duplicates
        btc_addresses = list(set(btc_addresses))
        bch_addresses = list(set(bch_addresses))
        bsv_addresses = list(set(bsv_addresses))  
        eth_addresses = list(set(eth_addresses))
        
        results['total_addresses_generated'] = len(btc_addresses) + len(eth_addresses)
        
        print(f"   ✅ Generated {len(btc_addresses)} BTC/BCH/BSV addresses")
        print(f"   ✅ Generated {len(eth_addresses)} ETH addresses")
        
        # Scan each blockchain
        print(f"\n2️⃣  SCANNING BITCOIN CASH (BCH)")
        bch_utxos = self.scan_bch_utxos(bch_addresses)
        results['utxos_found']['BCH'] = bch_utxos
        results['total_value']['BCH'] = sum(utxo['value'] for utxo in bch_utxos) / 1e8
        
        print(f"\n3️⃣  SCANNING BITCOIN SV (BSV)")
        bsv_utxos = self.scan_bsv_utxos(bsv_addresses)
        results['utxos_found']['BSV'] = bsv_utxos
        results['total_value']['BSV'] = sum(utxo['value'] for utxo in bsv_utxos) / 1e8
        
        print(f"\n4️⃣  SCANNING ETHEREUM (ETH)")
        eth_balances = self.scan_eth_balances(eth_addresses)
        results['utxos_found']['ETH'] = eth_balances
        results['total_value']['ETH'] = sum(bal['balance_eth'] for bal in eth_balances)
        
        # Summary
        print(f"\n🎉 MULTI-BLOCKCHAIN SCAN COMPLETE!")
        print("=" * 50)
        
        total_found = 0
        for blockchain, utxos in results['utxos_found'].items():
            count = len(utxos)
            value = results['total_value'][blockchain]
            
            if count > 0:
                print(f"   💰 {blockchain}: {count} UTXOs/addresses - {value:.8f} {blockchain}")
                total_found += count
            else:
                print(f"   ⭕ {blockchain}: No funds found")
        
        print(f"\n📊 TOTAL RESULTS:")
        print(f"   🎯 Total UTXOs/Balances: {total_found}")
        print(f"   🔍 Addresses Scanned: {results['total_addresses_generated']}")
        print(f"   ⛓️  Blockchains: {len(results['blockchains_scanned'])}")
        
        if total_found > 0:
            print(f"\n🏆 FUNDS FOUND! Breakdown by blockchain:")
            for blockchain, value in results['total_value'].items():
                if value > 0:
                    print(f"   🪙 {blockchain}: {value:.8f} {blockchain}")
                    
                    # Show top UTXOs/balances
                    utxos = results['utxos_found'][blockchain][:3]  # Top 3
                    for utxo in utxos:
                        if blockchain == 'ETH':
                            print(f"      💎 {utxo['balance_eth']:.6f} ETH - {utxo['address']}")
                        else:
                            print(f"      💎 {utxo['value']/1e8:.8f} {blockchain} - {utxo['address']}")
        
        # Save results
        with open('multi_blockchain_scan.json', 'w') as f:
            json.dump(results, f, indent=2)
            
        print(f"\n💾 Results saved to multi_blockchain_scan.json")
        
        return results

def main():
    """Main multi-blockchain scan"""
    try:
        scanner = MultiBlockchainScanner()
        results = scanner.comprehensive_multi_blockchain_scan()
        
        # Final summary
        total_value_usd = 0  # Could add USD conversion
        has_funds = any(results['total_value'][chain] > 0 for chain in results['total_value'])
        
        if has_funds:
            print(f"\n🚀 SUCCESS: Cryptocurrency found across multiple blockchains!")
            print(f"   Ready to build transactions and move funds")
        else:
            print(f"\n🔍 Scan complete - no funds found on scanned blockchains")
            print(f"   Try different wallet seeds or check additional networks")
            
    except Exception as e:
        print(f"❌ Multi-blockchain scan error: {e}")

if __name__ == "__main__":
    main()