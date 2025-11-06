#!/usr/bin/env python3
"""
UTXO Scanner - Find current, unspent UTXOs from wallet descriptors
"""

import requests
import time
import hashlib
import base58
from concurrent.futures import ThreadPoolExecutor, as_completed
from collections import defaultdict
import json

class UTXOScanner:
    """Scan for unspent UTXOs from wallet descriptors/addresses"""
    
    def __init__(self, max_workers=10):
        self.explorers = [
            {"name": "Blockstream", "base": "https://blockstream.info/api"},
            {"name": "Mempool.space", "base": "https://mempool.space/api"}
        ]
        self.max_workers = max_workers
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'UTXO-Scanner/1.0'
        })
        
    def scan_address(self, address, min_confirmations=1):
        """Scan a single address for UTXOs"""
        utxos = []
        
        for explorer in self.explorers:
            try:
                # Get UTXOs for address
                url = f"{explorer['base']}/address/{address}/utxo"
                response = self.session.get(url, timeout=15)
                
                if response.status_code == 200:
                    data = response.json()
                    
                    for utxo in data:
                        # Check confirmations
                        confirmations = utxo.get('status', {}).get('confirmations', 0)
                        if confirmations >= min_confirmations:
                            utxos.append({
                                'txid': utxo['txid'],
                                'vout': utxo['vout'],
                                'value': utxo['value'],
                                'address': address,
                                'confirmations': confirmations,
                                'block_height': utxo.get('status', {}).get('block_height'),
                                'explorer': explorer['name']
                            })
                    
                    return utxos
                    
            except Exception as e:
                print(f"   ❌ Error scanning {address} with {explorer['name']}: {e}")
                continue
                
        return utxos
    
    def scan_multiple_addresses(self, addresses, min_confirmations=1):
        """Scan multiple addresses in parallel"""
        print(f"🔍 Scanning {len(addresses)} addresses for UTXOs...")
        print(f"📊 Min confirmations: {min_confirmations}")
        
        all_utxos = []
        
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            # Submit scanning tasks
            future_to_address = {
                executor.submit(self.scan_address, addr, min_confirmations): addr 
                for addr in addresses
            }
            
            # Process results as they complete
            for future in as_completed(future_to_address):
                address = future_to_address[future]
                try:
                    utxos = future.result()
                    if utxos:
                        print(f"   ✅ {address}: {len(utxos)} UTXOs found")
                        for utxo in utxos:
                            print(f"      💰 {utxo['value']/100000000:.8f} BTC ({utxo['confirmations']} confs)")
                        all_utxos.extend(utxos)
                    else:
                        print(f"   ⭕ {address}: No UTXOs")
                except Exception as e:
                    print(f"   ❌ {address}: Error - {e}")
        
        return all_utxos
    
    def get_address_balance(self, address):
        """Get total balance for an address"""
        for explorer in self.explorers:
            try:
                url = f"{explorer['base']}/address/{address}"
                response = self.session.get(url, timeout=15)
                
                if response.status_code == 200:
                    data = response.json()
                    
                    # Different explorers have different response formats
                    if explorer['name'] == 'Blockstream':
                        confirmed = data['chain_stats']['funded_txo_sum'] - data['chain_stats']['spent_txo_sum']
                        unconfirmed = data['mempool_stats']['funded_txo_sum'] - data['mempool_stats']['spent_txo_sum']
                    else:  # Mempool.space
                        confirmed = data['chain_stats']['funded_txo_sum'] - data['chain_stats']['spent_txo_sum']
                        unconfirmed = data['mempool_stats']['funded_txo_sum'] - data['mempool_stats']['spent_txo_sum']
                    
                    return {
                        'confirmed': confirmed,
                        'unconfirmed': unconfirmed,
                        'total': confirmed + unconfirmed
                    }
                    
            except Exception as e:
                print(f"   ❌ Error getting balance for {address}: {e}")
                continue
                
        return {'confirmed': 0, 'unconfirmed': 0, 'total': 0}
    
    def select_utxos_largest_first(self, utxos, target_amount=None, max_utxos=10):
        """Select UTXOs using largest-first strategy"""
        # Sort by value (largest first)
        sorted_utxos = sorted(utxos, key=lambda x: x['value'], reverse=True)
        
        if target_amount is None:
            # Return the largest UTXOs
            return sorted_utxos[:max_utxos]
        
        # Select UTXOs to meet target amount
        selected = []
        total_value = 0
        
        for utxo in sorted_utxos:
            selected.append(utxo)
            total_value += utxo['value']
            
            if total_value >= target_amount:
                break
                
            if len(selected) >= max_utxos:
                break
        
        return selected
    
    def find_large_utxos(self, addresses, min_value_btc=0.001, min_confirmations=1):
        """Find large UTXOs above a minimum value"""
        print(f"🎯 Searching for UTXOs >= {min_value_btc} BTC...")
        
        min_value_sats = int(min_value_btc * 100000000)
        all_utxos = self.scan_multiple_addresses(addresses, min_confirmations)
        
        # Filter by minimum value
        large_utxos = [utxo for utxo in all_utxos if utxo['value'] >= min_value_sats]
        
        # Sort by value (largest first)
        large_utxos.sort(key=lambda x: x['value'], reverse=True)
        
        return large_utxos
    
    def generate_utxo_summary(self, utxos):
        """Generate a summary of UTXOs"""
        if not utxos:
            return "No UTXOs found"
        
        total_value = sum(utxo['value'] for utxo in utxos)
        total_btc = total_value / 100000000
        
        summary = f"""
🎯 UTXO SUMMARY
{'='*50}
💰 Total UTXOs: {len(utxos)}
🔥 Total Value: {total_btc:.8f} BTC ({total_value:,} sats)
📊 Average Size: {total_btc/len(utxos):.8f} BTC

🏆 TOP 10 LARGEST:
"""
        
        for i, utxo in enumerate(utxos[:10]):
            btc_value = utxo['value'] / 100000000
            summary += f"   {i+1:2d}. {btc_value:12.8f} BTC - {utxo['txid'][:16]}...:{utxo['vout']}\n"
            summary += f"       Address: {utxo['address'][:20]}... ({utxo['confirmations']} confs)\n"
        
        return summary

def scan_for_big_utxos():
    """Scan known large UTXO addresses (public addresses with known large balances)"""
    
    print("🔍 SCANNING FOR LARGE, AVAILABLE UTXOs")
    print("=" * 60)
    
    scanner = UTXOScanner()
    
    # Known addresses with historically large balances (public info)
    # These are examples - user will need to provide their own controlled addresses
    test_addresses = [
        "1FeexV6bAHb8ybZjqQMjJrcCrHGW9sb6uF",  # BitFinex cold wallet (example)
        "3D2oetdNuZUqQHPJmcMDDHYoqkyNVsFk9r",  # Large exchange wallet (example)
        "bc1qgdjqv0av3q56jvd82tkdjpy7gdp9ut8tlqmgrpmv24sq90ecnvqqjvxlu",  # Large P2WSH
    ]
    
    print(f"📋 Scanning {len(test_addresses)} known large addresses...")
    print("⚠️  NOTE: These are PUBLIC addresses for demonstration")
    print("⚠️  For actual use, provide addresses YOU CONTROL")
    print()
    
    # Find UTXOs > 0.01 BTC
    large_utxos = scanner.find_large_utxos(
        test_addresses,
        min_value_btc=0.01,
        min_confirmations=1
    )
    
    if large_utxos:
        print("\n" + scanner.generate_utxo_summary(large_utxos))
        
        # Select best UTXOs
        best_utxos = scanner.select_utxos_largest_first(large_utxos, max_utxos=5)
        
        print(f"\n🎯 RECOMMENDED UTXOs FOR TRANSACTION:")
        print("=" * 50)
        
        for utxo in best_utxos:
            btc_value = utxo['value'] / 100000000
            print(f"💎 {btc_value:12.8f} BTC")
            print(f"   TXID: {utxo['txid']}")
            print(f"   Output: {utxo['vout']}")
            print(f"   Address: {utxo['address']}")
            print(f"   Confirmations: {utxo['confirmations']}")
            print()
        
    else:
        print("\n❌ No large UTXOs found in scanned addresses")
        print("💡 Try providing your own wallet addresses or lowering min_value_btc")

if __name__ == "__main__":
    scan_for_big_utxos()