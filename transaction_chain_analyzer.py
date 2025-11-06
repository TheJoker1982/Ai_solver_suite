#!/usr/bin/env python3
"""
Transaction Chain Dependency Analyzer
Analyze chained Bitcoin transactions and determine broadcast order
"""

import hashlib
import struct
from io import BytesIO
from collections import defaultdict

class TransactionChainAnalyzer:
    """Analyze chained transactions for correct broadcast order"""
    
    def __init__(self):
        self.transactions = {}
        self.dependencies = defaultdict(list)
        self.outputs_created = {}  # txid:vout -> tx_id
        self.inputs_spent = defaultdict(list)  # tx_id -> [(prev_txid, prev_vout)]
        
    def add_transaction(self, tx_id, tx_hex):
        """Add a transaction to the dependency analysis"""
        parsed = self._parse_transaction(tx_hex)
        parsed['hex'] = tx_hex
        parsed['tx_id'] = tx_id
        
        self.transactions[tx_id] = parsed
        
        # Track inputs this transaction spends
        for inp in parsed['inputs']:
            prev_ref = (inp['prev_txid'], inp['prev_vout'])
            self.inputs_spent[tx_id].append(prev_ref)
            
            # If this input references an output we created, mark dependency
            if prev_ref in self.outputs_created:
                parent_tx = self.outputs_created[prev_ref]
                self.dependencies[parent_tx].append(tx_id)
        
        # Track outputs this transaction creates
        for i, output in enumerate(parsed['outputs']):
            output_ref = (parsed['txid'], i)
            self.outputs_created[output_ref] = tx_id
            
        return parsed
    
    def _parse_transaction(self, tx_hex):
        """Parse transaction and compute correct TXID (handling SegWit)"""
        raw_bytes = bytes.fromhex(tx_hex)
        stream = BytesIO(raw_bytes)
        
        # Read version
        version = struct.unpack('<I', stream.read(4))[0]
        
        # Check for SegWit marker/flag
        is_segwit = False
        marker_pos = stream.tell()
        marker = stream.read(1)[0]
        
        if marker == 0x00:  # SegWit marker
            flag = stream.read(1)[0]
            if flag == 0x01:  # SegWit flag
                is_segwit = True
            else:
                # Not SegWit, rewind
                stream.seek(marker_pos)
        else:
            # Not SegWit, rewind
            stream.seek(marker_pos)
        
        # Parse inputs
        num_inputs = self._read_varint(stream)
        inputs = []
        
        for _ in range(num_inputs):
            prev_txid = stream.read(32)[::-1].hex()  # Reverse for display
            prev_vout = struct.unpack('<I', stream.read(4))[0]
            script_len = self._read_varint(stream)
            script = stream.read(script_len)
            sequence = struct.unpack('<I', stream.read(4))[0]
            
            inputs.append({
                'prev_txid': prev_txid,
                'prev_vout': prev_vout,
                'script_sig': script.hex(),
                'sequence': sequence
            })
        
        # Parse outputs
        num_outputs = self._read_varint(stream)
        outputs = []
        
        for _ in range(num_outputs):
            value = struct.unpack('<Q', stream.read(8))[0]
            script_len = self._read_varint(stream)
            script = stream.read(script_len)
            
            outputs.append({
                'value': value,
                'script_pubkey': script.hex()
            })
        
        # Parse witness data (if SegWit)
        witnesses = []
        if is_segwit:
            for _ in range(num_inputs):
                witness_count = self._read_varint(stream)
                witness_stack = []
                for _ in range(witness_count):
                    witness_len = self._read_varint(stream)
                    witness_item = stream.read(witness_len)
                    witness_stack.append(witness_item.hex())
                witnesses.append(witness_stack)
        
        # Parse locktime
        locktime = struct.unpack('<I', stream.read(4))[0]
        
        # Compute correct TXID (without witness data for SegWit)
        if is_segwit:
            # Rebuild transaction without witness data for TXID calculation
            txid_bytes = self._build_legacy_format(version, inputs, outputs, locktime)
            txid = self._double_sha256(txid_bytes)[::-1].hex()
            
            # WTXID includes witness data
            wtxid = self._double_sha256(raw_bytes)[::-1].hex()
        else:
            # Legacy transaction - TXID is just double SHA256
            txid = self._double_sha256(raw_bytes)[::-1].hex()
            wtxid = txid
        
        return {
            'version': version,
            'inputs': inputs,
            'outputs': outputs,
            'witnesses': witnesses if is_segwit else None,
            'locktime': locktime,
            'is_segwit': is_segwit,
            'txid': txid,
            'wtxid': wtxid,
            'size': len(raw_bytes),
            'vsize': self._calculate_vsize(len(raw_bytes), len(witnesses) if is_segwit else 0)
        }
    
    def _build_legacy_format(self, version, inputs, outputs, locktime):
        """Build legacy transaction format (no witness) for TXID calculation"""
        result = b''
        
        # Version
        result += struct.pack('<I', version)
        
        # Input count
        result += self._encode_varint(len(inputs))
        
        # Inputs
        for inp in inputs:
            result += bytes.fromhex(inp['prev_txid'])[::-1]  # Reverse back
            result += struct.pack('<I', inp['prev_vout'])
            script_bytes = bytes.fromhex(inp['script_sig'])
            result += self._encode_varint(len(script_bytes))
            result += script_bytes
            result += struct.pack('<I', inp['sequence'])
        
        # Output count
        result += self._encode_varint(len(outputs))
        
        # Outputs
        for output in outputs:
            result += struct.pack('<Q', output['value'])
            script_bytes = bytes.fromhex(output['script_pubkey'])
            result += self._encode_varint(len(script_bytes))
            result += script_bytes
        
        # Locktime
        result += struct.pack('<I', locktime)
        
        return result
    
    def _read_varint(self, stream):
        """Read variable-length integer"""
        first = stream.read(1)[0]
        if first < 0xfd:
            return first
        elif first == 0xfd:
            return struct.unpack('<H', stream.read(2))[0]
        elif first == 0xfe:
            return struct.unpack('<I', stream.read(4))[0]
        else:
            return struct.unpack('<Q', stream.read(8))[0]
    
    def _encode_varint(self, n):
        """Encode variable-length integer"""
        if n < 0xfd:
            return struct.pack('B', n)
        elif n < 0x10000:
            return b'\xfd' + struct.pack('<H', n)
        elif n < 0x100000000:
            return b'\xfe' + struct.pack('<I', n)
        else:
            return b'\xff' + struct.pack('<Q', n)
    
    def _double_sha256(self, data):
        """Double SHA256 hash"""
        return hashlib.sha256(hashlib.sha256(data).digest()).digest()
    
    def _calculate_vsize(self, size, witness_count):
        """Calculate virtual size for fee calculation"""
        if witness_count == 0:
            return size
        else:
            # SegWit virtual size calculation
            base_size = size - witness_count  # Approximate
            return int((base_size * 3 + size) / 4)
    
    def analyze_dependencies(self):
        """Analyze transaction dependencies and determine broadcast order"""
        
        print("🔍 TRANSACTION CHAIN ANALYSIS")
        print("=" * 60)
        
        # Show all transactions
        for tx_id, tx in self.transactions.items():
            print(f"\n📋 Transaction {tx_id}:")
            print(f"   TXID: {tx['txid']}")
            print(f"   SegWit: {tx['is_segwit']}")
            if tx['is_segwit']:
                print(f"   WTXID: {tx['wtxid']}")
            print(f"   Inputs: {len(tx['inputs'])}")
            print(f"   Outputs: {len(tx['outputs'])} ({sum(o['value'] for o in tx['outputs'])/100000000:.2f} BTC)")
        
        # Build dependency graph
        print(f"\n🔗 DEPENDENCY ANALYSIS:")
        dependency_found = False
        
        for tx_id in self.transactions:
            for prev_txid, prev_vout in self.inputs_spent[tx_id]:
                # Check if this input references another transaction in our set
                for other_tx_id, other_tx in self.transactions.items():
                    if other_tx['txid'] == prev_txid:
                        print(f"   {other_tx_id} → {tx_id} (output {prev_vout})")
                        dependency_found = True
                        break
        
        if not dependency_found:
            print("   No dependencies found - transactions are independent")
        
        # Determine broadcast order using topological sort
        broadcast_order = self._topological_sort()
        
        print(f"\n📊 BROADCAST ORDER:")
        for i, tx_id in enumerate(broadcast_order):
            tx = self.transactions[tx_id]
            print(f"   {i+1}. {tx_id} (TXID: {tx['txid']})")
        
        return {
            'transactions': self.transactions,
            'dependencies': dict(self.dependencies),
            'broadcast_order': broadcast_order,
            'has_dependencies': dependency_found
        }
    
    def _topological_sort(self):
        """Topological sort for broadcast order"""
        # Count incoming edges
        in_degree = {tx_id: 0 for tx_id in self.transactions}
        
        for parent, children in self.dependencies.items():
            for child in children:
                in_degree[child] += 1
        
        # Find nodes with no incoming edges
        queue = [tx_id for tx_id, degree in in_degree.items() if degree == 0]
        result = []
        
        while queue:
            current = queue.pop(0)
            result.append(current)
            
            # Remove edges from current node
            for child in self.dependencies[current]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    queue.append(child)
        
        return result

def analyze_user_transaction_chain(tx1_hex, tx2_hex):
    """Analyze the user's transaction chain"""
    
    analyzer = TransactionChainAnalyzer()
    
    print("🚀 ANALYZING USER TRANSACTION CHAIN")
    print("=" * 70)
    
    # Add both transactions
    analyzer.add_transaction("TX1", tx1_hex)
    analyzer.add_transaction("TX2", tx2_hex) 
    
    # Analyze dependencies
    analysis = analyzer.analyze_dependencies()
    
    # Show recommended actions
    print(f"\n✅ RECOMMENDATIONS:")
    
    if analysis['has_dependencies']:
        print("   📋 CHAINED TRANSACTIONS DETECTED")
        print("   🔧 Broadcast in dependency order:")
        for i, tx_id in enumerate(analysis['broadcast_order']):
            tx = analysis['transactions'][tx_id]
            print(f"      {i+1}. {tx_id}: bitcoin-cli sendrawtransaction {tx['hex']}")
            print(f"         Creates TXID: {tx['txid']}")
    else:
        print("   📋 INDEPENDENT TRANSACTIONS")
        print("   🔧 Can broadcast in any order or simultaneously")
        for tx_id in analysis['broadcast_order']:
            tx = analysis['transactions'][tx_id]
            print(f"      {tx_id}: bitcoin-cli sendrawtransaction {tx['hex']}")
    
    return analysis

if __name__ == "__main__":
    print("🔧 Transaction Chain Analyzer Ready")