#!/usr/bin/env python3
"""
Blockchain State Checker - Check transaction status and timing
"""

import hashlib
import requests
import time
from datetime import datetime, timezone

class BlockchainStateChecker:
    """Check blockchain state and transaction timing"""
    
    def __init__(self):
        # Multiple API endpoints for redundancy
        self.explorers = [
            {"name": "BlockCypher", "base": "https://api.blockcypher.com/v1/btc/main"},
            {"name": "Blockstream", "base": "https://blockstream.info/api"},
            {"name": "Mempool.space", "base": "https://mempool.space/api"}
        ]
        
    def get_transaction_status(self, txid):
        """Get transaction status from blockchain explorers"""
        print(f"🔍 Checking transaction: {txid}")
        
        for explorer in self.explorers:
            try:
                if explorer["name"] == "BlockCypher":
                    url = f"{explorer['base']}/txs/{txid}"
                elif explorer["name"] == "Blockstream":
                    url = f"{explorer['base']}/tx/{txid}"
                elif explorer["name"] == "Mempool.space":
                    url = f"{explorer['base']}/tx/{txid}"
                
                print(f"   📡 Querying {explorer['name']}...")
                response = requests.get(url, timeout=10)
                
                if response.status_code == 200:
                    data = response.json()
                    
                    if explorer["name"] == "BlockCypher":
                        return self._parse_blockcypher_response(data)
                    elif explorer["name"] == "Blockstream":
                        return self._parse_blockstream_response(data)
                    elif explorer["name"] == "Mempool.space":
                        return self._parse_mempool_response(data)
                        
                elif response.status_code == 404:
                    print(f"   ❌ Transaction not found on {explorer['name']}")
                else:
                    print(f"   ⚠️  {explorer['name']} returned {response.status_code}")
                    
            except Exception as e:
                print(f"   ❌ Error with {explorer['name']}: {e}")
                continue
        
        return {
            'found': False,
            'confirmed': False,
            'block_height': None,
            'block_time': None,
            'fee': None
        }
    
    def _parse_blockcypher_response(self, data):
        """Parse BlockCypher API response"""
        return {
            'found': True,
            'confirmed': data.get('confirmations', 0) > 0,
            'confirmations': data.get('confirmations', 0),
            'block_height': data.get('block_height'),
            'block_time': data.get('confirmed') if data.get('confirmed') else None,
            'fee': data.get('fees'),
            'size': data.get('size'),
            'inputs': len(data.get('inputs', [])),
            'outputs': len(data.get('outputs', []))
        }
    
    def _parse_blockstream_response(self, data):
        """Parse Blockstream API response"""
        return {
            'found': True,
            'confirmed': 'status' in data and data['status'].get('confirmed', False),
            'confirmations': data['status'].get('confirmations', 0) if 'status' in data else 0,
            'block_height': data['status'].get('block_height') if 'status' in data else None,
            'block_time': data['status'].get('block_time') if 'status' in data else None,
            'fee': data.get('fee'),
            'size': data.get('size'),
            'weight': data.get('weight'),
            'inputs': len(data.get('vin', [])),
            'outputs': len(data.get('vout', []))
        }
    
    def _parse_mempool_response(self, data):
        """Parse Mempool.space API response"""
        return {
            'found': True,
            'confirmed': 'status' in data and data['status'].get('confirmed', False),
            'confirmations': data['status'].get('confirmations', 0) if 'status' in data else 0,
            'block_height': data['status'].get('block_height') if 'status' in data else None,
            'block_time': data['status'].get('block_time') if 'status' in data else None,
            'fee': data.get('fee'),
            'size': data.get('size'),
            'weight': data.get('weight'),
            'inputs': len(data.get('vin', [])),
            'outputs': len(data.get('vout', []))
        }
    
    def check_utxo_availability(self, txid, vout):
        """Check if a UTXO is available for spending"""
        print(f"💰 Checking UTXO: {txid}:{vout}")
        
        for explorer in self.explorers:
            try:
                if explorer["name"] == "Blockstream":
                    url = f"{explorer['base']}/tx/{txid}/outspent/{vout}"
                    response = requests.get(url, timeout=10)
                    
                    if response.status_code == 200:
                        data = response.json()
                        spent = data.get('spent', False)
                        
                        print(f"   📊 UTXO Status:")
                        print(f"      Spent: {spent}")
                        if spent:
                            print(f"      Spent in TX: {data.get('txid', 'Unknown')}")
                            print(f"      Spent at input: {data.get('vin', 'Unknown')}")
                        
                        return {
                            'available': not spent,
                            'spent': spent,
                            'spent_txid': data.get('txid') if spent else None,
                            'spent_vin': data.get('vin') if spent else None
                        }
                        
                elif explorer["name"] == "Mempool.space":
                    url = f"{explorer['base']}/tx/{txid}/outspend/{vout}"
                    response = requests.get(url, timeout=10)
                    
                    if response.status_code == 200:
                        data = response.json()
                        spent = data.get('spent', False)
                        
                        return {
                            'available': not spent,
                            'spent': spent,
                            'spent_txid': data.get('txid') if spent else None,
                            'spent_vin': data.get('vin') if spent else None
                        }
                        
            except Exception as e:
                print(f"   ❌ Error checking UTXO with {explorer['name']}: {e}")
                continue
        
        return {'available': None, 'spent': None}
    
    def get_current_block_info(self):
        """Get current blockchain info"""
        for explorer in self.explorers:
            try:
                if explorer["name"] == "Blockstream":
                    url = f"{explorer['base']}/blocks/tip/height"
                    response = requests.get(url, timeout=10)
                    if response.status_code == 200:
                        height = response.text.strip()
                        return {'height': int(height), 'timestamp': int(time.time())}
                        
                elif explorer["name"] == "Mempool.space":
                    url = f"{explorer['base']}/blocks/tip/height"  
                    response = requests.get(url, timeout=10)
                    if response.status_code == 200:
                        height = response.text.strip()
                        return {'height': int(height), 'timestamp': int(time.time())}
                        
            except Exception as e:
                print(f"❌ Error getting block info from {explorer['name']}: {e}")
                continue
        
        return {'height': None, 'timestamp': int(time.time())}

def analyze_transaction_timing(tx1_txid, tx2_txid, spending_tx_hex):
    """Analyze transaction timing and blockchain state"""
    
    print("⏰ BLOCKCHAIN STATE & TIMING ANALYSIS")
    print("=" * 70)
    
    checker = BlockchainStateChecker()
    
    # Get current block info
    block_info = checker.get_current_block_info()
    print(f"📊 Current Block: {block_info['height']} (as of {datetime.fromtimestamp(block_info['timestamp'])})")
    print()
    
    # Check both parent transactions
    print("🔍 PARENT TRANSACTION STATUS:")
    
    tx1_status = checker.get_transaction_status(tx1_txid)
    print(f"\n📋 TX1 ({tx1_txid}):")
    if tx1_status['found']:
        print(f"   ✅ Found in blockchain")
        print(f"   📊 Confirmed: {tx1_status['confirmed']}")
        if tx1_status['confirmed']:
            print(f"   🎯 Confirmations: {tx1_status['confirmations']}")
            print(f"   📦 Block: {tx1_status['block_height']}")
            if tx1_status['block_time']:
                try:
                    if isinstance(tx1_status['block_time'], str):
                        # Handle ISO format or other string formats
                        from dateutil.parser import parse
                        block_time = parse(tx1_status['block_time'])
                    else:
                        block_time = datetime.fromtimestamp(tx1_status['block_time'])
                    print(f"   ⏰ Block Time: {block_time}")
                except:
                    print(f"   ⏰ Block Time: {tx1_status['block_time']} (raw)")
    else:
        print(f"   ❌ NOT FOUND in blockchain")
    
    tx2_status = checker.get_transaction_status(tx2_txid)
    print(f"\n📋 TX2 ({tx2_txid}):")
    if tx2_status['found']:
        print(f"   ✅ Found in blockchain")
        print(f"   📊 Confirmed: {tx2_status['confirmed']}")
        if tx2_status['confirmed']:
            print(f"   🎯 Confirmations: {tx2_status['confirmations']}")
            print(f"   📦 Block: {tx2_status['block_height']}")
            if tx2_status['block_time']:
                try:
                    if isinstance(tx2_status['block_time'], str):
                        # Handle ISO format or other string formats
                        from dateutil.parser import parse
                        block_time = parse(tx2_status['block_time'])
                    else:
                        block_time = datetime.fromtimestamp(tx2_status['block_time'])
                    print(f"   ⏰ Block Time: {block_time}")
                except:
                    print(f"   ⏰ Block Time: {tx2_status['block_time']} (raw)")
    else:
        print(f"   ❌ NOT FOUND in blockchain")
    
    # Check UTXO availability  
    print(f"\n💰 UTXO AVAILABILITY CHECK:")
    
    if tx1_status['found'] and tx1_status['confirmed']:
        utxo1 = checker.check_utxo_availability(tx1_txid, 0)  # TX1 output 0
        print(f"   🎯 {tx1_txid}:0 - Available: {utxo1['available']}")
        if utxo1['spent']:
            print(f"      ⚠️  Already spent in: {utxo1['spent_txid']}")
    
    if tx2_status['found'] and tx2_status['confirmed']:
        utxo2 = checker.check_utxo_availability(tx2_txid, 1)  # TX2 output 1  
        print(f"   🎯 {tx2_txid}:1 - Available: {utxo2['available']}")
        if utxo2['spent']:
            print(f"      ⚠️  Already spent in: {utxo2['spent_txid']}")
    
    # Analyze timing requirements
    print(f"\n⏰ TIMING ANALYSIS:")
    
    if not tx1_status['found'] or not tx2_status['found']:
        print("   ❌ PARENT TRANSACTIONS NOT FOUND")
        print("   🔧 ACTION: Broadcast parent transactions first")
        return False
        
    if not tx1_status['confirmed'] or not tx2_status['confirmed']:
        print("   ⏳ PARENT TRANSACTIONS NOT CONFIRMED")
        print("   🔧 ACTION: Wait for confirmation before spending")
        return False
        
    # Check if UTXOs are already spent
    if tx1_status['found'] and tx1_status['confirmed']:
        utxo1 = checker.check_utxo_availability(tx1_txid, 0)
        if utxo1['spent']:
            print("   ❌ TX1 UTXO ALREADY SPENT")
            print("   🔧 ACTION: Transaction window has closed")
            return False
            
    if tx2_status['found'] and tx2_status['confirmed']:
        utxo2 = checker.check_utxo_availability(tx2_txid, 1) 
        if utxo2['spent']:
            print("   ❌ TX2 UTXO ALREADY SPENT") 
            print("   🔧 ACTION: Transaction window has closed")
            return False
    
    print("   ✅ TIMING WINDOW STILL OPEN")
    print("   🚀 ACTION: Ready to broadcast spending transaction")
    return True

if __name__ == "__main__":
    # Your transaction IDs
    tx1_txid = "f815694f58d6aa9a1d05368a39c148043ff2c987fd85bdcabbf7e98b6842cba2"
    tx2_txid = "b3436da6c530fd9cc0756a2c352f5e895e6af55e2f81b329a9817c42a2ffa4c0"
    spending_tx = "0100000002c0a4ffa2427c81a929b3812f5ef56a5e895e2f352c6a75c09cfd30c5a66d43b30100000000feffffffa2cb42688be9f7bbcabd85fd87c9f23f0448c1398a36051d9aaad6584f6915f80000000000feffffff02a8c634986e0000001976a9144356bb48f5ae0d34b3f116916f590b0fb8a2efd688aca8c634986e0000001976a9144356bb48f5ae0d34b3f116916f590b0fb8a2efd688ac00000000"
    
    result = analyze_transaction_timing(tx1_txid, tx2_txid, spending_tx)
    
    if result:
        print(f"\n🎯 READY FOR FINAL BROADCAST!")
    else:
        print(f"\n⚠️  NOT READY - Check timing requirements")