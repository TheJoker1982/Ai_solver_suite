#!/usr/bin/env python3
"""
WITNESS SCRIPT ANALYZER
Extracts and analyzes signature + public key from witness scripts
"""

import sys
import hashlib

def extract_signature_rs(sig_hex):
    """Extract R and S from DER signature"""
    sig = bytes.fromhex(sig_hex)
    
    # Skip 0x30 (compound), length
    pos = 2
    
    # R value
    if sig[pos] != 0x02:
        return None, None
    pos += 1
    r_len = sig[pos]
    pos += 1
    r_bytes = sig[pos:pos + r_len]
    r_value = int.from_bytes(r_bytes, 'big')
    pos += r_len
    
    # S value
    if sig[pos] != 0x02:
        return None, None
    pos += 1
    s_len = sig[pos]
    pos += 1
    s_bytes = sig[pos:pos + s_len]
    s_value = int.from_bytes(s_bytes, 'big')
    
    return r_value, s_value

def analyze_public_key(pubkey_hex):
    """Analyze compressed public key"""
    pubkey = bytes.fromhex(pubkey_hex)
    
    prefix = pubkey[0]
    x_coord = int.from_bytes(pubkey[1:], 'big')
    
    # Simple hash160 calculation (not full Bitcoin address derivation)
    sha256 = hashlib.sha256(pubkey).digest()
    hash160 = hashlib.new('ripemd160', sha256).digest()
    
    return {
        'prefix': f"0x{prefix:02x}",
        'x_coordinate': x_coord,
        'hash160': hash160.hex()
    }

def main():
    print("🔍 WITNESS SCRIPT ANALYZER")
    print("=" * 80)
    
    # The witness script provided
    witness_script = "473044022061d383f74bacc73e5df7f8c3f780c3cf1485c78d07313651e1af6a2f67862897022050eb836bffc9c2c3aa32746672faf3fe2cf8989e218fc617fc58fee14640622f0121022bccd43333d2ef5c805b1c60b9e525ff756acca60972374422cfb52a736b9145"
    
    print(f"📜 Witness Script: {witness_script}")
    print()
    
    # Extract components
    # 47 = push 71 bytes (signature)
    sig_len = int(witness_script[0:2], 16)
    sig_start = 2
    sig_end = sig_start + (sig_len * 2)
    signature = witness_script[sig_start:sig_end]
    
    # Next byte = push 33 bytes (public key)
    pubkey_len = int(witness_script[sig_end:sig_end+2], 16)
    pubkey_start = sig_end + 2
    pubkey = witness_script[pubkey_start:]
    
    print("=" * 80)
    print("📝 STRING #1: SIGNATURE")
    print("=" * 80)
    print(f"Hex: {signature}")
    print(f"Length: {len(signature) // 2} bytes")
    print()
    
    # Extract R and S
    r_value, s_value = extract_signature_rs(signature)
    
    if r_value and s_value:
        print("🔑 SIGNATURE COMPONENTS:")
        print(f"   R (hex): {r_value:064x}")
        print(f"   R (dec): {r_value}")
        print()
        print(f"   S (hex): {s_value:064x}")
        print(f"   S (dec): {s_value}")
        print()
        
        # Modular analysis
        print("📊 MODULAR ANALYSIS:")
        print(f"   R mod 71 = {r_value % 71}")
        print(f"   R mod 42 = {r_value % 42}")
        print(f"   R mod 8  = {r_value % 8}")
        print()
        print(f"   S mod 71 = {s_value % 71}")
        print(f"   S mod 42 = {s_value % 42}")
        print(f"   S mod 8  = {s_value % 8}")
        print()
        
        # XOR analysis
        xor_value = r_value ^ s_value
        print(f"   R ⊕ S = {xor_value}")
        print(f"   (R⊕S) mod 71 = {xor_value % 71}")
        print(f"   (R⊕S) mod 42 = {xor_value % 42}")
        print(f"   (R⊕S) mod 8  = {xor_value % 8}")
        print()
    
    print("=" * 80)
    print("📝 STRING #2: PUBLIC KEY")
    print("=" * 80)
    print(f"Hex: {pubkey}")
    print(f"Length: {len(pubkey) // 2} bytes")
    print()
    
    # Analyze public key
    pubkey_data = analyze_public_key(pubkey)
    
    print("🔑 PUBLIC KEY COMPONENTS:")
    print(f"   Prefix: {pubkey_data['prefix']} ({'Even Y' if pubkey_data['prefix'] == '0x02' else 'Odd Y'})")
    print(f"   X-coord (hex): {pubkey_data['x_coordinate']:064x}")
    print(f"   X-coord (dec): {pubkey_data['x_coordinate']}")
    print(f"   Hash160: {pubkey_data['hash160']}")
    print()
    
    # Check if X-coord has patterns
    x = pubkey_data['x_coordinate']
    print("📊 X-COORDINATE MODULAR ANALYSIS:")
    print(f"   X mod 71 = {x % 71}")
    print(f"   X mod 42 = {x % 42}")
    print(f"   X mod 8  = {x % 8}")
    print()
    
    # Check relationships
    if r_value and s_value:
        print("=" * 80)
        print("🔗 RELATIONSHIPS:")
        print("=" * 80)
        print(f"   R ⊕ X = {r_value ^ x}")
        print(f"   S ⊕ X = {s_value ^ x}")
        print(f"   (R+S) mod 71 = {(r_value + s_value) % 71}")
        print(f"   (R+X) mod 71 = {(r_value + x) % 71}")
        print(f"   (S+X) mod 71 = {(s_value + x) % 71}")
        print()
        
        # Check if any values are in Puzzle 71 range
        puzzle_71_start = 2**70
        puzzle_71_end = 2**71 - 1
        
        print("🎯 PUZZLE 71 RANGE CHECK (2^70 to 2^71-1):")
        print(f"   R in range: {puzzle_71_start <= r_value <= puzzle_71_end}")
        print(f"   S in range: {puzzle_71_start <= s_value <= puzzle_71_end}")
        print(f"   X in range: {puzzle_71_start <= x <= puzzle_71_end}")
        print(f"   R⊕S in range: {puzzle_71_start <= xor_value <= puzzle_71_end}")
        print()
    
    print("=" * 80)
    print("✅ ANALYSIS COMPLETE")
    print("=" * 80)

if __name__ == "__main__":
    main()
