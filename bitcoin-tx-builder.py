#!/usr/bin/env python3
"""
Bitcoin Transaction Builder with Manual Signing Support
Converts UTXO data into transaction and generates preimages for signing
"""

import struct
import hashlib
from typing import List, Dict, Any, Optional
from decimal import Decimal
import json

def base58_decode(s):
    """Decode Base58Check encoded string"""
    alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    
    # Convert from base58
    num = 0
    for char in s:
        num = num * 58 + alphabet.index(char)
    
    # Convert to bytes
    hex_str = hex(num)[2:].rstrip('L')
    if len(hex_str) % 2:
        hex_str = '0' + hex_str
    
    bytes_array = bytes.fromhex(hex_str)
    
    # Remove checksum and version byte
    if len(bytes_array) >= 25:
        return bytes_array[1:-4].hex()
    return None

def double_sha256(data):
    """Perform double SHA256 hash"""
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()

def encode_varint(n):
    """Encode a number as a variable-length integer"""
    if n < 0xfd:
        return struct.pack('<B', n)
    elif n <= 0xffff:
        return b'\xfd' + struct.pack('<H', n)
    elif n <= 0xffffffff:
        return b'\xfe' + struct.pack('<L', n)
    else:
        return b'\xff' + struct.pack('<Q', n)

class TransactionInput:
    """Represents a transaction input"""
    
    def __init__(self, txid: str, vout: int, script_sig: str = "", sequence: int = 0xffffffff):
        self.txid = txid
        self.vout = vout
        self.script_sig = script_sig
        self.sequence = sequence
        self.original_script_pubkey = ""  # Store the original scriptPubKey for signing
    
    def __str__(self):
        return f"Input: {self.txid}:{self.vout}"
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "txid": self.txid,
            "vout": self.vout,
            "script_sig": self.script_sig,
            "sequence": self.sequence
        }

class TransactionOutput:
    """Represents a transaction output"""
    
    def __init__(self, value: int, script_pubkey: str):
        self.value = value  # in satoshis
        self.script_pubkey = script_pubkey
    
    def __str__(self):
        return f"Output: {self.value} sats"
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "value": self.value,
            "script_pubkey": self.script_pubkey
        }

class BitcoinTransaction:
    """Bitcoin transaction builder with signing support"""
    
    def __init__(self, version: int = 1, locktime: int = 0):
        self.version = version
        self.inputs: List[TransactionInput] = []
        self.outputs: List[TransactionOutput] = []
        self.locktime = locktime
    
    def add_input(self, txid: str, vout: int, script_pubkey: str = "", sequence: int = 0xffffffff):
        """Add an input to the transaction"""
        inp = TransactionInput(txid, vout, "", sequence)
        inp.original_script_pubkey = script_pubkey
        self.inputs.append(inp)
    
    def add_output(self, value: int, script_pubkey: str):
        """Add an output to the transaction"""
        self.outputs.append(TransactionOutput(value, script_pubkey))
    
    def get_total_input_value(self, utxo_values: Dict[str, int]) -> int:
        """Calculate total input value from UTXO values"""
        total = 0
        for inp in self.inputs:
            key = f"{inp.txid}:{inp.vout}"
            if key in utxo_values:
                total += utxo_values[key]
        return total
    
    def get_total_output_value(self) -> int:
        """Calculate total output value"""
        return sum(output.value for output in self.outputs)
    
    def calculate_fee(self, utxo_values: Dict[str, int]) -> int:
        """Calculate transaction fee"""
        return self.get_total_input_value(utxo_values) - self.get_total_output_value()
    
    def serialize_for_signing(self, input_index: int, sighash_type: int = 1) -> bytes:
        """
        Serialize transaction for signing (generate preimage)
        
        Args:
            input_index: Index of input being signed
            sighash_type: Signature hash type (1 = SIGHASH_ALL)
        
        Returns:
            bytes: Serialized transaction ready for signing
        """
        result = b""
        
        # Version
        result += struct.pack('<I', self.version)
        
        # Input count
        result += encode_varint(len(self.inputs))
        
        # Inputs
        for i, inp in enumerate(self.inputs):
            # Previous output hash (reversed)
            result += bytes.fromhex(inp.txid)[::-1]
            
            # Previous output index
            result += struct.pack('<I', inp.vout)
            
            # Script
            if i == input_index:
                # For the input being signed, use the scriptPubKey of the output being spent
                script = bytes.fromhex(inp.original_script_pubkey)
            else:
                # For other inputs, use empty script
                script = b""
            
            result += encode_varint(len(script))
            result += script
            
            # Sequence
            result += struct.pack('<I', inp.sequence)
        
        # Output count
        result += encode_varint(len(self.outputs))
        
        # Outputs
        for output in self.outputs:
            # Value
            result += struct.pack('<Q', output.value)
            
            # Script
            script = bytes.fromhex(output.script_pubkey)
            result += encode_varint(len(script))
            result += script
        
        # Locktime
        result += struct.pack('<I', self.locktime)
        
        # Sighash type
        result += struct.pack('<I', sighash_type)
        
        return result
    
    def get_signature_hash(self, input_index: int, sighash_type: int = 1) -> bytes:
        """
        Get the hash that needs to be signed for a specific input
        
        Returns:
            bytes: 32-byte hash to be signed
        """
        preimage = self.serialize_for_signing(input_index, sighash_type)
        return double_sha256(preimage)
    
    def get_all_signature_hashes(self, sighash_type: int = 1) -> Dict[int, bytes]:
        """
        Get signature hashes for all inputs
        
        Returns:
            Dict mapping input index to signature hash
        """
        hashes = {}
        for i in range(len(self.inputs)):
            hashes[i] = self.get_signature_hash(i, sighash_type)
        return hashes
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert transaction to dictionary format"""
        return {
            "version": self.version,
            "locktime": self.locktime,
            "inputs": [inp.to_dict() for inp in self.inputs],
            "outputs": [out.to_dict() for out in self.outputs]
        }

def address_to_script_pubkey(address: str) -> str:
    """Convert Bitcoin address to scriptPubKey hex"""
    if address.startswith('1'):  # P2PKH address
        hash160 = base58_decode(address)
        if hash160:
            return f"76a914{hash160}88ac"
    return ""

def utxos_to_transaction_inputs(utxo_data: Dict[str, Any]) -> tuple:
    """
    Convert UTXO data to transaction inputs and create a mapping of values
    
    Returns:
        tuple: (list of TransactionInput objects, dict mapping "txid:vout" to values)
    """
    inputs = []
    utxo_values = {}
    
    for utxo in utxo_data["utxos"]:
        # Create transaction input
        tx_input = TransactionInput(
            txid=utxo["txid"],
            vout=utxo["vout"],
            script_sig="",  # Will be filled during signing
            sequence=utxo["sequence"]
        )
        tx_input.original_script_pubkey = utxo["script_pubkey"]
        inputs.append(tx_input)
        
        # Store value for fee calculation
        key = f"{utxo['txid']}:{utxo['vout']}"
        utxo_values[key] = utxo["value"]
    
    return inputs, utxo_values

def create_transaction_from_utxos(
    utxo_data: Dict[str, Any],
    recipient_address: str,
    send_amount: int,
    fee_rate: int = 10  # satoshis per byte
) -> BitcoinTransaction:
    """
    Create a transaction using all UTXOs, sending to recipient with change back
    
    Args:
        utxo_data: UTXO data from the JSON
        recipient_address: Recipient's Bitcoin address
        send_amount: Amount to send in satoshis
        fee_rate: Fee rate in satoshis per byte
    
    Returns:
        BitcoinTransaction object
    """
    
    # Create transaction
    tx = BitcoinTransaction()
    
    # Add all UTXOs as inputs
    inputs, utxo_values = utxos_to_transaction_inputs(utxo_data)
    for inp in inputs:
        tx.add_input(inp.txid, inp.vout, inp.original_script_pubkey, inp.sequence)
    
    # Calculate total available
    total_input_value = sum(utxo_values.values())
    
    # Estimate transaction size (rough estimate)
    # Each input ~148 bytes, each output ~34 bytes, overhead ~10 bytes
    estimated_size = len(inputs) * 148 + 2 * 34 + 10
    estimated_fee = estimated_size * fee_rate
    
    # Calculate change amount
    change_amount = total_input_value - send_amount - estimated_fee
    
    # Add recipient output
    recipient_script = address_to_script_pubkey(recipient_address)
    tx.add_output(send_amount, recipient_script)
    
    # Add change output if significant amount
    if change_amount > 546:  # Dust threshold
        # Use same script as the input address (from first UTXO)
        change_script = utxo_data["utxos"][0]["script_pubkey"]
        tx.add_output(change_amount, change_script)
    
    return tx

# Your UTXO data
utxo_data = {
    "address": "1NBC8uXJy1GiJ6drkiZa1WuKn51ps7EPTv",
    "utxo_count": 12,
    "total_value_satoshis": 1600119082,
    "total_value_btc": 16.00119082,
    "utxos": [
        {
            "txid": "12f34b58b04dfb0233ce889f674781c0e0c7ba95482cca469125af41a78d13b3",
            "vout": 84,
            "value": 1440000000,
            "satoshis": 1440000000,
            "value_btc": 14.4,
            "script_pubkey": "76a914e84818e1bf7f699aa6e28ef9edfb58209909929288ac",
            "address": "1NBC8uXJy1GiJ6drkiZa1WuKn51ps7EPTv",
            "sequence": 4294967295,
            "sequence_hex": "ffffffff"
        },
        {
            "txid": "5d45587cfd1d5b0fb826805541da7d94c61fe432259e68ee26f4a04544384164",
            "vout": 108,
            "value": 144000000,
            "satoshis": 144000000,
            "value_btc": 1.44,
            "script_pubkey": "76a914e84818e1bf7f699aa6e28ef9edfb58209909929288ac",
            "address": "1NBC8uXJy1GiJ6drkiZa1WuKn51ps7EPTv",
            "sequence": 4294967295,
            "sequence_hex": "ffffffff"
        },
        {
            "txid": "08389f34c98c606322740c0be6a7125d9860bb8d5cb182c02f98461e5fa6cd15",
            "vout": 159,
            "value": 16000000,
            "satoshis": 16000000,
            "value_btc": 0.16,
            "script_pubkey": "76a914e84818e1bf7f699aa6e28ef9edfb58209909929288ac",
            "address": "1NBC8uXJy1GiJ6drkiZa1WuKn51ps7EPTv",
            "sequence": 4294967295,
            "sequence_hex": "ffffffff"
        },
        {
            "txid": "ae3c5d4277175a604a125f7b4461a083ca1a4dcfd5110b4c77ee773dea7a6877",
            "vout": 1,
            "value": 100000,
            "satoshis": 100000,
            "value_btc": 0.001,
            "script_pubkey": "76a914e84818e1bf7f699aa6e28ef9edfb58209909929288ac",
            "address": "1NBC8uXJy1GiJ6drkiZa1WuKn51ps7EPTv",
            "sequence": 4294967295,
            "sequence_hex": "ffffffff"
        },
        {
            "txid": "9ad34108526a0491386df4055dae20456551288aba2a8893fccdd6842ab29f7e",
            "vout": 9,
            "value": 10000,
            "satoshis": 10000,
            "value_btc": 0.0001,
            "script_pubkey": "76a914e84818e1bf7f699aa6e28ef9edfb58209909929288ac",
            "address": "1NBC8uXJy1GiJ6drkiZa1WuKn51ps7EPTv",
            "sequence": 4294967295,
            "sequence_hex": "ffffffff"
        },
        {
            "txid": "f28d7dda479bc61ac34fc762226634e51135b6a6609b2a774e1e4495f9f996ed",
            "vout": 0,
            "value": 3768,
            "satoshis": 3768,
            "value_btc": 3.768e-05,
            "script_pubkey": "76a914e84818e1bf7f699aa6e28ef9edfb58209909929288ac",
            "address": "1NBC8uXJy1GiJ6drkiZa1WuKn51ps7EPTv",
            "sequence": 4294967295,
            "sequence_hex": "ffffffff"
        },
        {
            "txid": "6b2f1287b8e6f9b4394977a2d389313647ef0f004d6ef0f752a03d014a10a021",
            "vout": 0,
            "value": 1500,
            "satoshis": 1500,
            "value_btc": 1.5e-05,
            "script_pubkey": "76a914e84818e1bf7f699aa6e28ef9edfb58209909929288ac",
            "address": "1NBC8uXJy1GiJ6drkiZa1WuKn51ps7EPTv",
            "sequence": 4294967295,
            "sequence_hex": "ffffffff"
        },
        {
            "txid": "e2e8e1988044d6195dc6f076a9d5810eec4f3493667b536ddec898dcacc10d4f",
            "vout": 0,
            "value": 1000,
            "satoshis": 1000,
            "value_btc": 1e-05,
            "script_pubkey": "76a914e84818e1bf7f699aa6e28ef9edfb58209909929288ac",
            "address": "1NBC8uXJy1GiJ6drkiZa1WuKn51ps7EPTv",
            "sequence": 4294967295,
            "sequence_hex": "ffffffff"
        },
        {
            "txid": "4cab5e1213071d60d6e452a6b4e9caefbbae44611c3dc2bd757a639a1f85fdd2",
            "vout": 0,
            "value": 821,
            "satoshis": 821,
            "value_btc": 8.21e-06,
            "script_pubkey": "76a914e84818e1bf7f699aa6e28ef9edfb58209909929288ac",
            "address": "1NBC8uXJy1GiJ6drkiZa1WuKn51ps7EPTv",
            "sequence": 4294967295,
            "sequence_hex": "ffffffff"
        },
        {
            "txid": "336043f3a5f08e4f08dc25bf7ae61aa74d008641a55e4a8e37d2a71a2d0fbd65",
            "vout": 0,
            "value": 793,
            "satoshis": 793,
            "value_btc": 7.93e-06,
            "script_pubkey": "76a914e84818e1bf7f699aa6e28ef9edfb58209909929288ac",
            "address": "1NBC8uXJy1GiJ6drkiZa1WuKn51ps7EPTv",
            "sequence": 4294967295,
            "sequence_hex": "ffffffff"
        },
        {
            "txid": "d864c1a02f3ba7028d4a0723bc64102b04d3afea7e2a114e2d6db515489750ff",
            "vout": 0,
            "value": 600,
            "satoshis": 600,
            "value_btc": 6e-06,
            "script_pubkey": "76a914e84818e1bf7f699aa6e28ef9edfb58209909929288ac",
            "address": "1NBC8uXJy1GiJ6drkiZa1WuKn51ps7EPTv",
            "sequence": 4294967295,
            "sequence_hex": "ffffffff"
        },
        {
            "txid": "65ef98ecd6392c4add3fd280f322baa252b697a1b1ab240db0876f004a88a405",
            "vout": 0,
            "value": 600,
            "satoshis": 600,
            "value_btc": 6e-06,
            "script_pubkey": "76a914e84818e1bf7f699aa6e28ef9edfb58209909929288ac",
            "address": "1NBC8uXJy1GiJ6drkiZa1WuKn51ps7EPTv",
            "sequence": 4294967295,
            "sequence_hex": "ffffffff"
        }
    ]
}

if __name__ == "__main__":
    # Convert UTXOs to transaction inputs
    inputs, utxo_values = utxos_to_transaction_inputs(utxo_data)
    
    print("=== UTXO Summary ===")
    print(f"Total UTXOs: {len(inputs)}")
    print(f"Total Value: {sum(utxo_values.values())} satoshis ({sum(utxo_values.values()) / 100000000} BTC)")
    
    # Create transaction to your receiving address
    recipient_address = "14k121hBepgcTzL6VcDsFdr5HmWs9cTbp9"
    send_amount = 1549991600  # Send almost all, leaving room for fees
    
    tx = create_transaction_from_utxos(utxo_data, recipient_address, send_amount)
    
    print(f"\n=== Transaction Summary ===")
    print(f"Recipient: {recipient_address}")
    print(f"Send Amount: {send_amount} satoshis ({send_amount / 100000000} BTC)")
    print(f"Total Input Value: {tx.get_total_input_value(utxo_values)} sats")
    print(f"Total Output Value: {tx.get_total_output_value()} sats")
    print(f"Fee: {tx.calculate_fee(utxo_values)} sats")
    print(f"Number of Inputs: {len(tx.inputs)}")
    print(f"Number of Outputs: {len(tx.outputs)}")
    
    # Get signature hashes for manual signing
    print(f"\n=== Signature Hashes for Manual Signing ===")
    sig_hashes = tx.get_all_signature_hashes()
    
    for i, (input_idx, sig_hash) in enumerate(sig_hashes.items()):
        inp = tx.inputs[input_idx]
        print(f"\nInput {input_idx} ({inp.txid}:{inp.vout}):")
        print(f"  Signature Hash: {sig_hash.hex()}")
        
        # Also get the full preimage for reference
        preimage = tx.serialize_for_signing(input_idx)
        print(f"  Preimage: {preimage.hex()}")
        print(f"  Preimage Length: {len(preimage)} bytes")
    
    # Output the unsigned transaction in JSON format
    print(f"\n=== Unsigned Transaction (JSON) ===")
    tx_json = {
        "version": tx.version,
        "locktime": tx.locktime,
        "ins": []
    }
    
    for inp in tx.inputs:
        key = f"{inp.txid}:{inp.vout}"
        value = utxo_values[key]
        tx_json["ins"].append({
            "n": inp.vout,
            "script": {
                "asm": "",  # Will be filled during signing
                "hex": inp.script_sig
            },
            "sequence": inp.sequence,
            "txid": inp.txid,
            "witness": []
        })
    
    tx_json["outs"] = []
    for i, out in enumerate(tx.outputs):
        # Determine if this is the change output or recipient output
        if out.script_pubkey == address_to_script_pubkey(recipient_address):
            address_type = recipient_address
        else:
            address_type = utxo_data["address"]  # Change back to source
        
        tx_json["outs"].append({
            "n": i,
            "script": {
                "addresses": [address_type],
                "asm": "OP_DUP OP_HASH160 " + out.script_pubkey[6:-4] + " OP_EQUALVERIFY OP_CHECKSIG",
                "hex": out.script_pubkey
            },
            "value": out.value
        })
    
    print(json.dumps(tx_json, indent=2))
    
    # Instructions for manual signing
    print(f"\n=== Manual Signing Instructions ===")
    print("1. Use the signature hashes above with your private key")
    print("2. Sign each hash with ECDSA using your private key")
    print("3. Append SIGHASH_ALL (0x01) to each signature")
    print("4. Create script_sig for each input: [signature] [public_key]")
    print("5. Replace the empty script.hex values with the signed scripts")
    print("6. Serialize the final transaction for broadcasting")
    
    print(f"\nExpected script_sig format:")
    print(f"[signature_length][signature][pubkey_length][public_key]")
    print(f"Example: 47[signature]01 21[public_key]")