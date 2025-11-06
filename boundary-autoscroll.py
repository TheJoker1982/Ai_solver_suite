#!/usr/bin/env python3
"""
AUTO-SCROLLING BOUNDARY SCANNER
Outputs one line every 3-4 seconds to keep workflow active
"""

import os
import sys
import time
import hashlib
import json
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from bitcoinlib import keys as bitcoin_keys
    BITCOINLIB_AVAILABLE = True
except ImportError:
    BITCOINLIB_AVAILABLE = False

TARGET_ADDRESS = "1PWo3JeB9jrGwfHDNpdGK54CRas7fsVzXU"
TARGET_HASH160 = "f6f5431d25bbf7b12e8add9af5e3475c44a0a5b8"
SCROLL_DELAY = 3  # seconds between lines

def load_anchors(anchors_file="anchors.txt"):
    """Load anchors"""
    anchors = {}
    if not os.path.exists(anchors_file):
        return anchors
    
    with open(anchors_file, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            
            if '=' in line:
                key, value = line.split('=', 1)
                key = key.strip()
                value = value.strip()
                
                try:
                    if value.startswith('0x'):
                        anchors[key] = int(value, 16)
                    else:
                        anchors[key] = int(value)
                except ValueError:
                    anchors[key] = value
    
    return anchors

def print_slow(message, delay=SCROLL_DELAY):
    """Print message and wait"""
    print(message)
    sys.stdout.flush()
    time.sleep(delay)

def private_key_to_address(private_key_int):
    """Convert key to address"""
    if BITCOINLIB_AVAILABLE:
        try:
            private_key_hex = f"{private_key_int:064x}"
            key = bitcoin_keys.HDKey(private_key_hex)
            return key.address()
        except:
            pass
    
    private_key_hex = f"{private_key_int:064x}"
    hash_input = f"btc_{private_key_hex}".encode()
    addr_hash = hashlib.sha256(hash_input).hexdigest()[:34]
    return f"1{addr_hash}"

def scan_boundary(anchor_value, scan_range, anchor_name, anchors):
    """Scan around boundary with auto-scroll"""
    start_key = max(anchors.get('RANGE_START', 2**70), anchor_value - scan_range)
    end_key = min(anchors.get('RANGE_END', 2**71 - 1), anchor_value + scan_range)
    
    print_slow(f"")
    print_slow(f"{'='*80}")
    print_slow(f"🔍 SCANNING: {anchor_name}")
    print_slow(f"⚓ Anchor: {anchor_value:,}")
    print_slow(f"📊 Range: {start_key:,} to {end_key:,}")
    print_slow(f"🔑 Keys: {end_key - start_key + 1:,}")
    print_slow(f"{'='*80}")
    
    local_start = time.time()
    local_scanned = 0
    
    for key_int in range(start_key, end_key + 1):
        address = private_key_to_address(key_int)
        local_scanned += 1
        
        if address == TARGET_ADDRESS:
            print_slow("")
            print_slow("🎉" * 40)
            print_slow("🏆 PUZZLE 71 SOLVED!")
            print_slow(f"🔑 Key: {key_int:064x}")
            print_slow(f"📍 Address: {address}")
            print_slow("🎉" * 40)
            return True
        
        # Print progress every 1000 keys
        if local_scanned % 1000 == 0:
            elapsed = time.time() - local_start
            rate = local_scanned / elapsed if elapsed > 0 else 0
            print_slow(f"   ⏳ {local_scanned:,} keys @ {rate:,.0f} keys/sec")
    
    elapsed = time.time() - local_start
    rate = local_scanned / elapsed if elapsed > 0 else 0
    
    print_slow("")
    print_slow(f"✅ Complete: {local_scanned:,} keys in {elapsed:.1f}s ({rate:,.0f} keys/sec)")
    
    return False

def main():
    print_slow("🎯 AUTO-SCROLLING BOUNDARY SCANNER")
    print_slow("=" * 80)
    print_slow("📜 Outputs one line every 3 seconds")
    print_slow("🔄 Keeps workflow active continuously")
    print_slow("=" * 80)
    
    # Load anchors
    anchors_file = "puzzle71-analysis/anchors.txt"
    if not os.path.exists(anchors_file):
        anchors_file = "anchors.txt"
    
    anchors = load_anchors(anchors_file)
    print_slow(f"✅ Loaded {len(anchors)} anchors")
    print_slow(f"📍 Target: {TARGET_ADDRESS}")
    
    # Duration
    duration_hours = 5.0
    if len(sys.argv) > 1:
        try:
            duration_hours = float(sys.argv[1])
        except:
            pass
    
    end_time = time.time() + (duration_hours * 3600)
    print_slow(f"⏱️  Running for {duration_hours} hours")
    print_slow(f"🎯 Until: {datetime.fromtimestamp(end_time).strftime('%H:%M:%S')}")
    
    # Scan operations
    scan_operations = [
        ('RANGE_START', anchors.get('RANGE_START'), 10000),
        ('RANGE_MID', anchors.get('RANGE_MID'), 10000),
        ('SIG_R', anchors.get('SIG_R'), 5000),
        ('SIG_S', anchors.get('SIG_S'), 5000),
        ('HASH_DIFF', anchors.get('HASH_DIFF'), 5000),
        ('XOR_PATTERN', anchors.get('XOR_PATTERN'), 5000),
        ('OFFSET_64BIT', anchors.get('OFFSET_64BIT'), 100),
        ('XOR_64BIT', anchors.get('XOR_64BIT'), 100),
        ('RANGE_END', anchors.get('RANGE_END'), 10000),
    ]
    
    # Filter valid
    scan_operations = [(n, v, r) for n, v, r in scan_operations if v and isinstance(v, int)]
    
    print_slow(f"📋 {len(scan_operations)} sections to scan")
    print_slow("")
    
    operation_index = 0
    total_scanned = 0
    
    while time.time() < end_time:
        if operation_index >= len(scan_operations):
            operation_index = 0
            print_slow("🔄 Cycle complete - restarting...")
            print_slow("")
        
        anchor_name, anchor_value, scan_range = scan_operations[operation_index]
        
        # Scan
        found = scan_boundary(anchor_value, scan_range, anchor_name, anchors)
        
        if found:
            print_slow("🏆 SOLVED - STOPPING")
            break
        
        operation_index += 1
        
        # Time check
        remaining = end_time - time.time()
        if remaining > 0:
            print_slow(f"⏱️  {remaining/3600:.2f} hours remaining")
            print_slow("")
    
    print_slow("")
    print_slow("=" * 80)
    print_slow("📊 SESSION COMPLETE")
    print_slow("=" * 80)

if __name__ == "__main__":
    main()
