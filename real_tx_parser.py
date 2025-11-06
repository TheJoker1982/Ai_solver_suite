#!/usr/bin/env python3
"""
Real Bitcoin Transaction Parser
Extract UTXOs from user's real transaction hex
"""

import struct
from io import BytesIO

class BitcoinTransactionParser:
    """Parse real Bitcoin transaction hex to extract UTXO data"""
    
    def __init__(self, tx_hex):
        self.tx_hex = tx_hex
        self.raw_bytes = bytes.fromhex(tx_hex)
        self.stream = BytesIO(self.raw_bytes)
        
    def read_varint(self):
        """Read variable-length integer"""
        first_byte = self.stream.read(1)[0]
        if first_byte < 0xfd:
            return first_byte
        elif first_byte == 0xfd:
            return struct.unpack('<H', self.stream.read(2))[0]
        elif first_byte == 0xfe:
            return struct.unpack('<I', self.stream.read(4))[0]
        else:
            return struct.unpack('<Q', self.stream.read(8))[0]
    
    def parse_transaction(self):
        """Parse the complete transaction"""
        
        # Version (4 bytes)
        version = struct.unpack('<I', self.stream.read(4))[0]
        
        # Number of inputs
        num_inputs = self.read_varint()
        
        inputs = []
        print(f"🔍 PARSING REAL TRANSACTION")
        print(f"📊 Version: {version}")
        print(f"📊 Number of inputs: {num_inputs}")
        
        # Parse inputs
        for i in range(num_inputs):
            # Previous transaction hash (32 bytes, reversed for display)
            prev_hash = self.stream.read(32)[::-1].hex()
            
            # Previous output index (4 bytes)
            prev_index = struct.unpack('<I', self.stream.read(4))[0]
            
            # Script length
            script_len = self.read_varint()
            
            # Script (signature + pubkey)
            script = self.stream.read(script_len).hex()
            
            # Sequence (4 bytes)
            sequence = struct.unpack('<I', self.stream.read(4))[0]
            
            input_data = {
                'txid': prev_hash,
                'vout': prev_index,
                'script_sig': script,
                'sequence': sequence,
                'input_index': i
            }
            
            inputs.append(input_data)
            
            print(f"📋 Input {i+1}:")
            print(f"   TXID: {prev_hash}")
            print(f"   VOUT: {prev_index}")
            print(f"   Script Length: {script_len}")
        
        # Parse outputs
        num_outputs = self.read_varint()
        outputs = []
        
        print(f"\\n📊 Number of outputs: {num_outputs}")
        
        for i in range(num_outputs):
            # Value (8 bytes)
            value = struct.unpack('<Q', self.stream.read(8))[0]
            
            # Script length
            script_len = self.read_varint()
            
            # Script
            script = self.stream.read(script_len).hex()
            
            output_data = {
                'value': value,
                'script_pubkey': script,
                'output_index': i
            }
            
            outputs.append(output_data)
            
            print(f"📋 Output {i+1}:")
            print(f"   Value: {value/100000000:.8f} BTC ({value} satoshis)")
            print(f"   Script: {script}")
        
        # Locktime (4 bytes)
        locktime = struct.unpack('<I', self.stream.read(4))[0]
        
        return {
            'version': version,
            'inputs': inputs,
            'outputs': outputs,
            'locktime': locktime,
            'num_inputs': num_inputs,
            'num_outputs': num_outputs
        }
    
    def find_large_utxos(self, parsed_tx):
        """Find UTXOs suitable for 12K and 9K BTC transaction"""
        
        print(f"\\n🎯 ANALYZING OUTPUTS FOR LARGE UTXOS")
        
        large_outputs = []
        
        for output in parsed_tx['outputs']:
            btc_value = output['value'] / 100000000
            if btc_value >= 1000:  # Look for outputs >= 1000 BTC
                large_outputs.append({
                    'value': output['value'],
                    'btc_value': btc_value,
                    'output_index': output['output_index'],
                    'script': output['script_pubkey']
                })
        
        # Sort by value descending
        large_outputs.sort(key=lambda x: x['value'], reverse=True)
        
        print(f"📊 Found {len(large_outputs)} large outputs:")
        for i, output in enumerate(large_outputs):
            print(f"   {i+1}. {output['btc_value']:,.2f} BTC (Output {output['output_index']})")
        
        return large_outputs
    
    def get_transaction_hash(self):
        """Calculate transaction hash for UTXO references"""
        import hashlib
        
        # Double SHA256
        hash1 = hashlib.sha256(self.raw_bytes).digest()
        hash2 = hashlib.sha256(hash1).digest()
        
        # Reverse for display (Bitcoin convention)
        tx_hash = hash2[::-1].hex()
        
        return tx_hash

def parse_user_transaction(tx_hex):
    """Parse user's real transaction and prepare UTXO data"""
    
    print("🔧 PARSING YOUR REAL BITCOIN TRANSACTION")
    print("=" * 60)
    
    parser = BitcoinTransactionParser(tx_hex)
    parsed_tx = parser.parse_transaction()
    
    # Get transaction hash
    tx_hash = parser.get_transaction_hash()
    print(f"\\n🔗 Transaction Hash: {tx_hash}")
    
    # Find large outputs that could be our UTXOs
    large_outputs = parser.find_large_utxos(parsed_tx)
    
    if len(large_outputs) >= 2:
        # Use the two largest outputs as our UTXOs
        utxo_1 = {
            'txid': tx_hash,
            'vout': large_outputs[0]['output_index'],
            'value': large_outputs[0]['value']
        }
        
        utxo_2 = {
            'txid': tx_hash,
            'vout': large_outputs[1]['output_index'], 
            'value': large_outputs[1]['value']
        }
        
        print(f"\\n✅ EXTRACTED UTXO DATA:")
        print(f"📋 UTXO 1: {utxo_1['value']/100000000:,.2f} BTC")
        print(f"   TXID: {utxo_1['txid']}")
        print(f"   VOUT: {utxo_1['vout']}")
        print(f"📋 UTXO 2: {utxo_2['value']/100000000:,.2f} BTC")
        print(f"   TXID: {utxo_2['txid']}")
        print(f"   VOUT: {utxo_2['vout']}")
        
        return utxo_1, utxo_2, parsed_tx
    
    else:
        print(f"❌ Not enough large outputs found")
        return None, None, parsed_tx

if __name__ == "__main__":
    # Test with placeholder
    print("🔧 Real Transaction Parser Ready")