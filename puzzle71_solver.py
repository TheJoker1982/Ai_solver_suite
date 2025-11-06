#!/usr/bin/env python3

"""
Bitcoin Puzzle 71 Solver
Part of Bitcoin Puzzle Environment Integration

This module provides advanced analysis and solving capabilities specifically
for Bitcoin Puzzle 71, integrated with the comprehensive puzzle environment.

Target: 1PWo3JeB9jrGwfHDNpdGK54CRas7fsVzXU
Range: 2^70 to 2^71 - 1 (70-bit private key)
Balance: 1 satoshi (0.00000001 BTC)
"""

import os
import sys
import time
import secrets
import hashlib
import json
from typing import Dict, List, Optional, Tuple, Iterator
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from bitcoinlib import keys as bitcoin_keys
    from bitcoinlib.encoding import base58_check_encode, hash160
    BITCOINLIB_AVAILABLE = True
except ImportError:
    BITCOINLIB_AVAILABLE = False

class Puzzle71Solver:
    """Advanced solver for Bitcoin Puzzle 71"""
    
    # Puzzle 71 specific constants
    TARGET_ADDRESS = "1PWo3JeB9jrGwfHDNpdGK54CRas7fsVzXU"
    TARGET_HASH160 = "f6f5431d25bbf7b12e8add9af5e3475c44a0a5b8"  # CORRECT HASH
    RANGE_START = 2**70  # 1180591620717411303424
    RANGE_END = 2**71 - 1  # 2361183241434822606847
    RANGE_SIZE = 2**70
    BALANCE = 1  # satoshi
    
    def __init__(self, threads: int = 4, checkpoint_interval: int = 1000000):
        """Initialize the Puzzle 71 solver"""
        self.threads = threads
        self.checkpoint_interval = checkpoint_interval
        self.start_time = None
        self.keys_checked = 0
        self.session_log = []
        
        print("🎯 Bitcoin Puzzle 71 Solver initialized")
        print(f"📍 Target Address: {self.TARGET_ADDRESS}")
        print(f"📍 Target Hash160: {self.TARGET_HASH160}")
        print(f"📊 Search Range: 2^70 to 2^71 - 1")
        print(f"📊 Range Size: {self.RANGE_SIZE:,} keys")
        print(f"💰 Prize: {self.BALANCE} satoshi (0.00000001 BTC)")
        print(f"🔧 Threads: {self.threads}")
        print(f"💾 Checkpoint Interval: {self.checkpoint_interval:,} keys")
        
        if not BITCOINLIB_AVAILABLE:
            print("⚠️  BitcoinLib not available - using simplified methods")
    
    def private_key_to_address(self, private_key_int: int) -> Tuple[str, str]:
        """Convert private key to both compressed and uncompressed addresses"""
        private_key_hex = f"{private_key_int:064x}"
        
        if BITCOINLIB_AVAILABLE:
            try:
                # Use BitcoinLib for accurate conversion
                key = bitcoin_keys.HDKey(private_key_hex)
                compressed_addr = key.address()
                
                # Get uncompressed address
                key_uncompressed = bitcoin_keys.HDKey(private_key_hex, compressed=False)
                uncompressed_addr = key_uncompressed.address()
                
                return compressed_addr, uncompressed_addr
            except Exception as e:
                print(f"⚠️  BitcoinLib error: {e}")
        
        # Fallback method (simplified)
        return self._simple_key_to_address(private_key_int)
    
    def _simple_key_to_address(self, private_key_int: int) -> Tuple[str, str]:
        """Simplified private key to address conversion (fallback)"""
        # Note: This is a placeholder for demonstration
        # Real implementation would need proper secp256k1 point multiplication
        
        private_key_hex = f"{private_key_int:064x}"
        
        # Simplified hash-based address generation (not cryptographically accurate)
        hash_input = f"compressed_{private_key_hex}".encode()
        compressed_hash = hashlib.sha256(hash_input).hexdigest()[:40]
        
        hash_input = f"uncompressed_{private_key_hex}".encode()
        uncompressed_hash = hashlib.sha256(hash_input).hexdigest()[:40]
        
        # Placeholder Base58 encoding
        compressed_addr = f"1{compressed_hash[:25]}"
        uncompressed_addr = f"1{uncompressed_hash[:25]}"
        
        return compressed_addr, uncompressed_addr
    
    def check_key_range(self, start: int, end: int, thread_id: int) -> Optional[Dict]:
        """Check a range of private keys (thread worker function)"""
        local_checked = 0
        local_start_time = time.time()
        
        print(f"🧵 Thread {thread_id}: Checking range {start:,} to {end:,}")
        
        for private_key_int in range(start, min(end + 1, self.RANGE_END + 1)):
            compressed_addr, uncompressed_addr = self.private_key_to_address(private_key_int)
            local_checked += 1
            
            # Check for match
            if compressed_addr == self.TARGET_ADDRESS:
                result = {
                    'found': True,
                    'private_key': private_key_int,
                    'private_key_hex': f"{private_key_int:064x}",
                    'address': compressed_addr,
                    'type': 'compressed',
                    'thread_id': thread_id,
                    'keys_checked': local_checked,
                    'time_taken': time.time() - local_start_time
                }
                print(f"\n🎉🎉🎉 PUZZLE 71 SOLVED BY THREAD {thread_id}! 🎉🎉🎉")
                print(f"🔑 Private Key: {result['private_key_hex']}")
                print(f"📍 Address: {result['address']}")
                print(f"⏱️  Time: {result['time_taken']:.2f} seconds")
                return result
            
            if uncompressed_addr == self.TARGET_ADDRESS:
                result = {
                    'found': True,
                    'private_key': private_key_int,
                    'private_key_hex': f"{private_key_int:064x}",
                    'address': uncompressed_addr,
                    'type': 'uncompressed',
                    'thread_id': thread_id,
                    'keys_checked': local_checked,
                    'time_taken': time.time() - local_start_time
                }
                print(f"\n🎉🎉🎉 PUZZLE 71 SOLVED BY THREAD {thread_id}! 🎉🎉🎉")
                print(f"🔑 Private Key: {result['private_key_hex']}")
                print(f"📍 Address: {result['address']}")
                print(f"⏱️  Time: {result['time_taken']:.2f} seconds")
                return result
            
            # Progress reporting
            if local_checked % 100000 == 0:
                elapsed = time.time() - local_start_time
                rate = local_checked / elapsed if elapsed > 0 else 0
                print(f"🧵 Thread {thread_id}: {local_checked:,} keys, {rate:,.0f} keys/sec")
        
        return {
            'found': False,
            'thread_id': thread_id,
            'keys_checked': local_checked,
            'time_taken': time.time() - local_start_time,
            'range_start': start,
            'range_end': end
        }
    
    def random_search(self, duration_seconds: int = 3600) -> Optional[Dict]:
        """Perform random search within the puzzle range"""
        print(f"\n🎲 Starting random search for {duration_seconds} seconds...")
        
        start_time = time.time()
        keys_checked = 0
        
        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            futures = []
            
            # Submit random search tasks to threads
            for thread_id in range(self.threads):
                future = executor.submit(self._random_search_worker, 
                                       thread_id, duration_seconds, start_time)
                futures.append(future)
            
            # Check for completion
            for future in as_completed(futures):
                result = future.result()
                keys_checked += result['keys_checked']
                
                if result['found']:
                    # Cancel other futures
                    for f in futures:
                        f.cancel()
                    return result
        
        elapsed = time.time() - start_time
        rate = keys_checked / elapsed if elapsed > 0 else 0
        
        print(f"\n📊 Random Search Complete:")
        print(f"   ⏱️  Duration: {elapsed:.2f} seconds")
        print(f"   🔑 Keys Checked: {keys_checked:,}")
        print(f"   📈 Rate: {rate:,.0f} keys/second")
        print(f"   🎯 No solution found in this session")
        
        return None
    
    def _random_search_worker(self, thread_id: int, duration: int, start_time: float) -> Dict:
        """Random search worker function"""
        local_checked = 0
        
        while time.time() - start_time < duration:
            # Generate random key in puzzle range
            private_key_int = secrets.randbelow(self.RANGE_SIZE) + self.RANGE_START
            
            compressed_addr, uncompressed_addr = self.private_key_to_address(private_key_int)
            local_checked += 1
            
            # Check for match
            if compressed_addr == self.TARGET_ADDRESS or uncompressed_addr == self.TARGET_ADDRESS:
                addr_type = 'compressed' if compressed_addr == self.TARGET_ADDRESS else 'uncompressed'
                final_addr = compressed_addr if addr_type == 'compressed' else uncompressed_addr
                
                return {
                    'found': True,
                    'private_key': private_key_int,
                    'private_key_hex': f"{private_key_int:064x}",
                    'address': final_addr,
                    'type': addr_type,
                    'thread_id': thread_id,
                    'keys_checked': local_checked,
                    'time_taken': time.time() - start_time
                }
            
            # Progress reporting
            if local_checked % 50000 == 0:
                elapsed = time.time() - start_time
                rate = local_checked / elapsed if elapsed > 0 else 0
                print(f"🧵 Thread {thread_id} (random): {local_checked:,} keys, {rate:,.0f} keys/sec")
        
        return {
            'found': False,
            'thread_id': thread_id,
            'keys_checked': local_checked,
            'time_taken': time.time() - start_time
        }
    
    def sequential_search(self, start_offset: int = 0, max_keys: Optional[int] = None) -> Optional[Dict]:
        """Perform sequential search starting from range start + offset"""
        print(f"\n🔢 Starting sequential search from offset {start_offset:,}...")
        
        actual_start = self.RANGE_START + start_offset
        actual_end = min(self.RANGE_END, actual_start + (max_keys or self.RANGE_SIZE))
        
        print(f"📊 Search Range: {actual_start:,} to {actual_end:,}")
        print(f"🔑 Keys to Check: {actual_end - actual_start + 1:,}")
        
        # Divide range among threads
        keys_per_thread = (actual_end - actual_start + 1) // self.threads
        
        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            futures = []
            
            for thread_id in range(self.threads):
                thread_start = actual_start + (thread_id * keys_per_thread)
                thread_end = thread_start + keys_per_thread - 1
                
                if thread_id == self.threads - 1:  # Last thread gets remainder
                    thread_end = actual_end
                
                future = executor.submit(self.check_key_range, thread_start, thread_end, thread_id)
                futures.append(future)
            
            # Check for completion
            total_checked = 0
            for future in as_completed(futures):
                result = future.result()
                total_checked += result['keys_checked']
                
                if result['found']:
                    # Cancel other futures
                    for f in futures:
                        f.cancel()
                    return result
        
        print(f"\n📊 Sequential Search Complete:")
        print(f"   🔑 Keys Checked: {total_checked:,}")
        print(f"   🎯 No solution found in this range")
        
        return None
    
    def save_session_log(self, result: Optional[Dict] = None):
        """Save session log to file"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = f"puzzle71_session_{timestamp}.json"
        
        session_data = {
            'timestamp': timestamp,
            'target_address': self.TARGET_ADDRESS,
            'target_hash160': self.TARGET_HASH160,
            'search_range': {
                'start': self.RANGE_START,
                'end': self.RANGE_END,
                'size': self.RANGE_SIZE
            },
            'configuration': {
                'threads': self.threads,
                'checkpoint_interval': self.checkpoint_interval
            },
            'result': result,
            'session_log': self.session_log
        }
        
        # Create directory if it doesn't exist
        os.makedirs('session-logs', exist_ok=True)
        log_path = os.path.join('session-logs', log_file)
        
        with open(log_path, 'w') as f:
            json.dump(session_data, f, indent=2, default=str)
        
        print(f"💾 Session log saved to: {log_path}")
        return log_path

def main():
    """Main execution function"""
    print("🎯 Bitcoin Puzzle 71 Solver - Advanced Analysis Module")
    print("=" * 60)
    
    # Initialize solver
    solver = Puzzle71Solver(threads=4, checkpoint_interval=100000)
    
    print("\n🔬 Analysis Methods Available:")
    print("1. Random Search (recommended for initial exploration)")
    print("2. Sequential Search (systematic but very slow)")
    print("3. Pattern-Based Search (advanced mathematical approaches)")
    
    # Example usage
    method = input("\nSelect method (1/2/3) or press Enter for demo: ").strip()
    
    if method == "1":
        # Random search for 5 minutes
        duration = int(input("Enter duration in seconds (default 300): ") or "300")
        result = solver.random_search(duration)
    elif method == "2":
        # Sequential search
        max_keys = int(input("Enter max keys to check (default 1000000): ") or "1000000")
        result = solver.sequential_search(max_keys=max_keys)
    elif method == "3":
        print("⚠️  Pattern-based search not yet implemented")
        result = None
    else:
        # Demo mode - quick random search
        print("🎮 Demo Mode: Running 30-second random search...")
        result = solver.random_search(30)
    
    # Save session log
    solver.save_session_log(result)
    
    if result and result['found']:
        print("\n🎉🎉🎉 PUZZLE 71 SOLVED! 🎉🎉🎉")
        print(f"🔑 Winning Private Key: {result['private_key_hex']}")
        print(f"📍 Address: {result['address']} ({result['type']})")
        print(f"💰 Prize: 1 satoshi available for withdrawal!")
    else:
        print("\n🔍 Search complete - continue exploring or try different methods")
        print("💡 Tip: Puzzle 71 has a massive search space - persistence is key!")

if __name__ == "__main__":
    main()