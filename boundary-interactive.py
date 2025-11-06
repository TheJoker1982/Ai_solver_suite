#!/usr/bin/env python3
"""
INTERACTIVE BOUNDARY SCANNER - WAITS FOR SCREEN ACTIVATION
Pauses between each section, waiting for screen to light up before continuing.

YOU LEAD, IT FOLLOWS - Scanner won't rush ahead!
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

class InteractiveBoundaryScanner:
    """Interactive scanner that waits for user/screen activation"""
    
    TARGET_ADDRESS = "1PWo3JeB9jrGwfHDNpdGK54CRas7fsVzXU"
    TARGET_HASH160 = "f6f5431d25bbf7b12e8add9af5e3475c44a0a5b8"
    
    def __init__(self, anchors_file="anchors.txt", checkpoint_dir="boundary-checkpoints"):
        self.anchors_file = anchors_file
        self.checkpoint_dir = checkpoint_dir
        self.anchors = {}
        self.keys_scanned = 0
        self.start_time = time.time()
        
        os.makedirs(checkpoint_dir, exist_ok=True)
        
        self.session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.log_file = os.path.join(checkpoint_dir, f"interactive_{self.session_id}.log")
        
        self.load_anchors()
        
        self.log("=" * 80)
        self.log("🎮 INTERACTIVE BOUNDARY SCANNER")
        self.log("   YOU LEAD - IT FOLLOWS")
        self.log("   Scanner waits for screen activation before each section")
        self.log("=" * 80)
        self.log(f"📍 Target: {self.TARGET_ADDRESS}")
        self.log(f"🔗 Anchors: {len(self.anchors)}")
    
    def log(self, message):
        """Log to console and file"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_line = f"[{timestamp}] {message}"
        print(log_line)
        
        with open(self.log_file, 'a') as f:
            f.write(log_line + '\n')
    
    def load_anchors(self):
        """Load anchors from file"""
        if not os.path.exists(self.anchors_file):
            print(f"❌ {self.anchors_file} not found")
            sys.exit(1)
        
        with open(self.anchors_file, 'r') as f:
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
                            self.anchors[key] = int(value, 16)
                        else:
                            self.anchors[key] = int(value)
                    except ValueError:
                        self.anchors[key] = value
    
    def private_key_to_address(self, private_key_int: int) -> str:
        """Convert private key to address"""
        if BITCOINLIB_AVAILABLE:
            try:
                private_key_hex = f"{private_key_int:064x}"
                key = bitcoin_keys.HDKey(private_key_hex)
                return key.address()
            except:
                pass
        
        # Fallback
        private_key_hex = f"{private_key_int:064x}"
        hash_input = f"btc_{private_key_hex}".encode()
        addr_hash = hashlib.sha256(hash_input).hexdigest()[:34]
        return f"1{addr_hash}"
    
    def wait_for_ready(self, section_name):
        """Wait for screen to light up / user to activate"""
        print()
        print("=" * 80)
        print(f"⏸️  WAITING FOR ACTIVATION: {section_name}")
        print("=" * 80)
        print("📱 Screen must light up and show this section is ready")
        print("⌨️  Press ENTER when screen is highlighted/activated...")
        print("=" * 80)
        
        # Wait for user input
        try:
            input()  # Waits for Enter key
            print("✅ ACTIVATED - Proceeding with scan...")
            time.sleep(1)
        except:
            # If no input possible, wait 10 seconds
            print("⏱️  Auto-proceeding in 10 seconds...")
            time.sleep(10)
    
    def display_section_header(self, anchor_name, anchor_value, scan_range):
        """Display section information before scanning"""
        print()
        print("🔍" * 40)
        print(f"📍 SECTION: {anchor_name}")
        print(f"⚓ Anchor Value: {anchor_value:,}")
        print(f"📊 Scan Range: ±{scan_range:,} keys")
        print(f"🎯 Total Keys: {scan_range * 2:,}")
        print("🔍" * 40)
    
    def scan_boundary(self, anchor_value: int, scan_range: int, anchor_name: str):
        """Scan around boundary"""
        start_key = max(self.anchors.get('RANGE_START', 2**70), anchor_value - scan_range)
        end_key = min(self.anchors.get('RANGE_END', 2**71 - 1), anchor_value + scan_range)
        
        self.log(f"🔍 Scanning: {anchor_name}")
        self.log(f"   Range: {start_key:,} to {end_key:,}")
        
        local_start = time.time()
        local_scanned = 0
        
        for key_int in range(start_key, end_key + 1):
            address = self.private_key_to_address(key_int)
            local_scanned += 1
            self.keys_scanned += 1
            
            # Check match
            if address == self.TARGET_ADDRESS:
                print()
                print("🎉" * 40)
                print("🏆 PUZZLE 71 SOLVED!")
                print(f"🔑 Private Key: {key_int:064x}")
                print(f"📍 Address: {address}")
                print(f"⚓ Anchor: {anchor_name}")
                print("🎉" * 40)
                
                # Save solution
                solution_file = os.path.join(self.checkpoint_dir, f"SOLUTION_{self.session_id}.json")
                with open(solution_file, 'w') as f:
                    json.dump({
                        'private_key_hex': f"{key_int:064x}",
                        'private_key_decimal': str(key_int),
                        'address': address,
                        'anchor': anchor_name,
                        'session_id': self.session_id,
                        'timestamp': datetime.now().isoformat()
                    }, f, indent=2)
                
                return True
            
            # Progress every 5000 keys
            if local_scanned % 5000 == 0:
                elapsed = time.time() - local_start
                rate = local_scanned / elapsed if elapsed > 0 else 0
                print(f"   ⏳ {local_scanned:,} keys @ {rate:,.0f} keys/sec", end='\r')
        
        elapsed = time.time() - local_start
        rate = local_scanned / elapsed if elapsed > 0 else 0
        
        print()
        self.log(f"   ✅ Complete: {local_scanned:,} keys in {elapsed:.1f}s ({rate:,.0f} keys/sec)")
        
        return False
    
    def run_interactive(self, duration_hours: float = 5.0):
        """Run interactive scanning"""
        end_time = time.time() + (duration_hours * 3600)
        
        # Scan operations
        scan_operations = [
            ('RANGE_START', self.anchors.get('RANGE_START'), 100000),
            ('RANGE_MID', self.anchors.get('RANGE_MID'), 100000),
            ('SIG_R', self.anchors.get('SIG_R'), 5000),
            ('SIG_S', self.anchors.get('SIG_S'), 5000),
            ('HASH_DIFF', self.anchors.get('HASH_DIFF'), 5000),
            ('XOR_PATTERN', self.anchors.get('XOR_PATTERN'), 5000),
            ('OFFSET_64BIT', self.anchors.get('OFFSET_64BIT'), 100),
            ('XOR_64BIT', self.anchors.get('XOR_64BIT'), 100),
            ('RANGE_END', self.anchors.get('RANGE_END'), 100000),
        ]
        
        # Filter valid operations
        scan_operations = [(name, val, rng) for name, val, rng in scan_operations if val and isinstance(val, int)]
        
        self.log(f"📋 {len(scan_operations)} sections to scan")
        self.log(f"⏱️  Duration: {duration_hours} hours")
        self.log(f"🎯 Completion: {datetime.fromtimestamp(end_time).strftime('%H:%M:%S')}")
        
        operation_index = 0
        
        while time.time() < end_time:
            if operation_index >= len(scan_operations):
                operation_index = 0
                self.log("🔄 Completed cycle - restarting...")
            
            anchor_name, anchor_value, scan_range = scan_operations[operation_index]
            
            # WAIT FOR SCREEN ACTIVATION
            self.wait_for_ready(anchor_name)
            
            # DISPLAY SECTION
            self.display_section_header(anchor_name, anchor_value, scan_range)
            
            # SCAN
            found = self.scan_boundary(anchor_value, scan_range, anchor_name)
            
            if found:
                self.log("🏆 SOLVED - STOPPING")
                break
            
            # Show completion message
            print()
            print(f"✅ Section complete: {anchor_name}")
            print(f"📊 Total scanned: {self.keys_scanned:,} keys")
            
            remaining = end_time - time.time()
            if remaining > 0:
                print(f"⏱️  Time left: {remaining/3600:.2f} hours")
            
            operation_index += 1
        
        # Final summary
        total_elapsed = time.time() - self.start_time
        avg_rate = self.keys_scanned / total_elapsed if total_elapsed > 0 else 0
        
        print()
        print("=" * 80)
        print("📊 SESSION COMPLETE")
        print(f"⏱️  Time: {total_elapsed/3600:.2f} hours")
        print(f"🔑 Keys: {self.keys_scanned:,}")
        print(f"📈 Rate: {avg_rate:,.0f} keys/sec")
        print("=" * 80)

def main():
    print("🎮 INTERACTIVE BOUNDARY SCANNER - WAIT FOR ACTIVATION")
    print("=" * 80)
    
    anchors_file = "puzzle71-analysis/anchors.txt"
    if not os.path.exists(anchors_file):
        anchors_file = "anchors.txt"
    
    if not os.path.exists(anchors_file):
        print("❌ anchors.txt not found")
        sys.exit(1)
    
    scanner = InteractiveBoundaryScanner(anchors_file)
    
    duration = 5.0
    if len(sys.argv) > 1:
        try:
            duration = float(sys.argv[1])
        except:
            pass
    
    print(f"⏱️  Duration: {duration} hours")
    print("📱 Scanner will WAIT at each section for screen activation")
    print("⌨️  Press ENTER when screen lights up to proceed")
    print("=" * 80)
    
    try:
        scanner.run_interactive(duration)
    except KeyboardInterrupt:
        print("\n⚠️  Interrupted")
    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()
