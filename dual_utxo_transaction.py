#!/usr/bin/env python3
"""
Dual UTXO Bitcoin Transaction Builder
12,000 BTC + 9,000 BTC -> 50/50 Split with QR Codes
"""

import struct
import hashlib
import base58
from qr_generator import create_50_50_split_qrs

# Constants
RECIPIENT_ADDRESS = "1794B4ynTe3WA6VdCQWjg5EtPnYRuYZ45j"
CHANGE_ADDRESS = "12ib7dApVFvg82TXKycWBNpN8kFyiAN1dr"  # For any change

# Transaction parameters  
DUST_THRESHOLD = 546  # satoshis
DEFAULT_FEE_RATE = 10  # sat/byte
MAX_TX_SIZE = 100000  # bytes

class DualUTXOTransaction:
    """Build transaction from 2 large UTXOs with 50/50 split"""
    
    def __init__(self):
        self.utxos = []
        self.outputs = []
        self.fee = 0
        
    def set_utxos(self, utxo_12k, utxo_9k):
        """Set the two UTXOs (12,000 BTC and 9,000 BTC)"""
        
        # Validate UTXO structure
        required_fields = ['txid', 'vout', 'value']
        
        for utxo, name in [(utxo_12k, "12K UTXO"), (utxo_9k, "9K UTXO")]:
            for field in required_fields:
                if field not in utxo:
                    raise ValueError(f"{name} missing field: {field}")
            
            # Validate txid format
            if len(utxo['txid']) != 64:
                raise ValueError(f"{name} invalid txid length: {len(utxo['txid'])}")
            
            # Validate hex
            try:
                bytes.fromhex(utxo['txid'])
            except ValueError:
                raise ValueError(f"{name} invalid txid hex format")
        
        self.utxos = [utxo_12k, utxo_9k]
        
        print(f"✅ UTXOs Set:")
        print(f"  UTXO 1: {utxo_12k['value']/100000000:.8f} BTC ({utxo_12k['txid'][:16]}...)")
        print(f"  UTXO 2: {utxo_9k['value']/100000000:.8f} BTC ({utxo_9k['txid'][:16]}...)")
        
    def calculate_50_50_split(self):
        """Calculate 50/50 split of total value minus fees"""
        
        if not self.utxos:
            raise ValueError("UTXOs not set")
        
        # Total input value
        total_value = sum(utxo['value'] for utxo in self.utxos)
        
        # Estimate transaction size (2 inputs, 2 outputs)
        # Input: 32+4+1+4 = 41 bytes (unsigned) + ~108 bytes when signed = ~149 bytes each
        # Output: 8+1+25 = 34 bytes each (P2PKH)
        # Base: 4+1+1+4 = 10 bytes
        estimated_size = 10 + (149 * 2) + (34 * 2)  # ~366 bytes
        
        # Calculate fee
        estimated_fee = estimated_size * DEFAULT_FEE_RATE
        
        # Available for splitting
        spendable = total_value - estimated_fee
        
        # 50/50 split
        split_amount = spendable // 2
        
        # Any remainder goes to first output
        remainder = spendable % 2
        
        self.outputs = [
            {
                'address': RECIPIENT_ADDRESS,
                'amount': split_amount + remainder,
                'label': 'Payment 1 (50% + remainder)'
            },
            {
                'address': RECIPIENT_ADDRESS, 
                'amount': split_amount,
                'label': 'Payment 2 (50%)'
            }
        ]
        
        self.fee = estimated_fee
        
        print(f"\n💰 TRANSACTION CALCULATION:")
        print(f"Total Input:  {total_value/100000000:.8f} BTC")
        print(f"Fee:          {self.fee/100000000:.8f} BTC ({DEFAULT_FEE_RATE} sat/byte)")
        print(f"Split Amount: {split_amount/100000000:.8f} BTC each")
        print(f"Output 1:     {self.outputs[0]['amount']/100000000:.8f} BTC")
        print(f"Output 2:     {self.outputs[1]['amount']/100000000:.8f} BTC")
        
        return {
            'total_input': total_value,
            'fee': self.fee,
            'outputs': self.outputs,
            'estimated_size': estimated_size
        }
    
    def build_unsigned_transaction(self):
        """Build unsigned transaction hex"""
        
        if not self.utxos or not self.outputs:
            raise ValueError("UTXOs and outputs must be set first")
        
        # Transaction version (4 bytes, little endian)
        version = struct.pack('<I', 1)
        
        # Number of inputs
        num_inputs = struct.pack('B', len(self.utxos))
        
        # Build inputs
        inputs_data = b''
        for utxo in self.utxos:
            # Previous transaction hash (32 bytes, reversed)
            prev_hash = bytes.fromhex(utxo['txid'])[::-1]
            # Previous output index (4 bytes, little endian)  
            prev_index = struct.pack('<I', utxo['vout'])
            # Script length (empty for unsigned)
            script_len = struct.pack('B', 0)
            # Sequence
            sequence = struct.pack('<I', 0xfffffffe)
            
            inputs_data += prev_hash + prev_index + script_len + sequence
        
        # Number of outputs
        num_outputs = struct.pack('B', len(self.outputs))
        
        # Build outputs
        outputs_data = b''
        for output in self.outputs:
            # Amount (8 bytes, little endian)
            amount_bytes = struct.pack('<Q', output['amount'])
            # ScriptPubKey
            script = self._address_to_scriptpubkey(output['address'])
            script_bytes = bytes.fromhex(script)
            script_len = struct.pack('B', len(script_bytes))
            
            outputs_data += amount_bytes + script_len + script_bytes
        
        # Locktime
        locktime = struct.pack('<I', 0)
        
        # Combine transaction
        raw_tx = version + num_inputs + inputs_data + num_outputs + outputs_data + locktime
        
        return raw_tx.hex()
    
    def _address_to_scriptpubkey(self, address):
        """Convert Bitcoin address to scriptPubKey hex"""
        
        try:
            # Decode Base58Check
            decoded = base58.b58decode_check(address)
            
            # Extract version byte and pubkey hash
            version = decoded[0]
            pubkey_hash = decoded[1:]
            
            if version == 0x00:  # P2PKH mainnet
                # OP_DUP OP_HASH160 <pubkey_hash> OP_EQUALVERIFY OP_CHECKSIG
                script = "76a914" + pubkey_hash.hex() + "88ac"
                return script
            else:
                raise ValueError(f"Unsupported address version: {version}")
                
        except Exception as e:
            raise ValueError(f"Invalid address format: {e}")
    
    def create_transaction_with_qrs(self):
        """Complete transaction creation with QR codes"""
        
        # Calculate split
        calculation = self.calculate_50_50_split()
        
        # Build transaction
        tx_hex = self.build_unsigned_transaction()
        
        print(f"\n🔧 UNSIGNED TRANSACTION HEX:")
        print(f"{tx_hex}")
        
        print(f"\n📱 GENERATING QR CODES...")
        
        # Calculate total BTC for QR generation
        total_output_btc = sum(output['amount'] for output in self.outputs) / 100000000
        
        # Generate QR codes
        qr_summary = create_50_50_split_qrs(
            RECIPIENT_ADDRESS,
            total_output_btc,
            tx_hex
        )
        
        return {
            'transaction_hex': tx_hex,
            'calculation': calculation,
            'qr_codes': qr_summary,
            'ready_for_broadcast': True
        }

# Test function for when real UTXOs are provided
def create_real_transaction(utxo_12k_data, utxo_9k_data):
    """Create transaction with real UTXO data"""
    
    print("🚀 CREATING REAL DUAL-UTXO TRANSACTION")
    print("=" * 60)
    
    tx_builder = DualUTXOTransaction()
    
    try:
        # Set UTXOs
        tx_builder.set_utxos(utxo_12k_data, utxo_9k_data)
        
        # Create transaction and QRs
        result = tx_builder.create_transaction_with_qrs()
        
        print(f"\n✅ TRANSACTION READY FOR BROADCAST")
        print(f"📋 Hex: {result['transaction_hex']}")
        print(f"💰 Total Value: {(result['calculation']['total_input']/100000000):.8f} BTC")
        print(f"💸 Fee: {(result['calculation']['fee']/100000000):.8f} BTC")
        print(f"📱 QR Codes: {len(result['qr_codes'])} generated")
        
        return result
        
    except Exception as e:
        print(f"❌ Error creating transaction: {e}")
        return None

# Example structure - waiting for your real data
EXAMPLE_UTXO_STRUCTURE = {
    "utxo_12k": {
        "txid": "YOUR_REAL_TXID_64_CHARS_HERE_12K_UTXO",
        "vout": 0,  # Your real output index
        "value": 1200000000000  # 12,000 BTC in satoshis
    },
    "utxo_9k": {
        "txid": "YOUR_REAL_TXID_64_CHARS_HERE_9K_UTXO", 
        "vout": 1,  # Your real output index
        "value": 900000000000   # 9,000 BTC in satoshis
    }
}

if __name__ == "__main__":
    print("🔧 DUAL UTXO TRANSACTION BUILDER READY")
    print("📋 Waiting for real UTXO data...")
    print("📍 Structure needed:", EXAMPLE_UTXO_STRUCTURE)