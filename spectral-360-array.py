#!/usr/bin/env python3
"""
FULL 360° SPECTRAL ARRAY ANALYSIS
Comprehensive mathematical analysis from every angle
"""

import math

def spectral_analysis_360(value, sig_r, sig_s, pubkey_x):
    """360-degree spectral array analysis"""
    
    print("=" * 80)
    print("🌈 FULL 360° SPECTRAL ARRAY")
    print("=" * 80)
    print()
    
    # SECP256K1 constants
    CURVE_ORDER = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
    PUZZLE_71_START = 2**70
    PUZZLE_71_END = 2**71 - 1
    
    results = []
    
    # ========== ANGLE 0°-45°: BASIC OPERATIONS ==========
    print("🔵 ANGLE 0°-45°: BASIC ARITHMETIC")
    print("-" * 80)
    
    ops = [
        ("value", value),
        ("value + R", (value + sig_r) % (2**256)),
        ("value + S", (value + sig_s) % (2**256)),
        ("value + X", (value + pubkey_x) % (2**256)),
        ("value - R", (value - sig_r) % (2**256)),
        ("value - S", (value - sig_s) % (2**256)),
        ("R - value", (sig_r - value) % (2**256)),
        ("S - value", (sig_s - value) % (2**256)),
        ("value * 2", (value * 2) % (2**256)),
        ("value * 3", (value * 3) % (2**256)),
        ("value // 2", value // 2),
        ("value // 3", value // 3),
    ]
    
    for name, val in ops:
        mod71 = val % 71
        in_range = PUZZLE_71_START <= val <= PUZZLE_71_END
        print(f"   {name:20s} mod 71 = {mod71:3d}  {'🎯' if in_range else '  '}")
        if in_range:
            results.append((name, val, mod71))
    print()
    
    # ========== ANGLE 45°-90°: XOR OPERATIONS ==========
    print("🟢 ANGLE 45°-90°: XOR SPECTRAL")
    print("-" * 80)
    
    xor_ops = [
        ("value ⊕ R", value ^ sig_r),
        ("value ⊕ S", value ^ sig_s),
        ("value ⊕ X", value ^ pubkey_x),
        ("value ⊕ (R+S)", value ^ ((sig_r + sig_s) % (2**256))),
        ("(value⊕R) ⊕ S", (value ^ sig_r) ^ sig_s),
        ("R ⊕ S ⊕ value", sig_r ^ sig_s ^ value),
    ]
    
    for name, val in xor_ops:
        mod71 = val % 71
        in_range = PUZZLE_71_START <= val <= PUZZLE_71_END
        print(f"   {name:20s} mod 71 = {mod71:3d}  {'🎯' if in_range else '  '}")
        if in_range:
            results.append((name, val, mod71))
    print()
    
    # ========== ANGLE 90°-135°: MULTIPLICATIVE ==========
    print("🟡 ANGLE 90°-135°: MULTIPLICATIVE SPECTRAL")
    print("-" * 80)
    
    mult_ops = [
        ("value * R mod n", (value * sig_r) % CURVE_ORDER),
        ("value * S mod n", (value * sig_s) % CURVE_ORDER),
        ("value * X mod n", (value * pubkey_x) % CURVE_ORDER),
        ("R * S mod n", (sig_r * sig_s) % CURVE_ORDER),
        ("(R*S) ⊕ value", ((sig_r * sig_s) % CURVE_ORDER) ^ value),
    ]
    
    for name, val in mult_ops:
        mod71 = val % 71
        in_range = PUZZLE_71_START <= val <= PUZZLE_71_END
        print(f"   {name:20s} mod 71 = {mod71:3d}  {'🎯' if in_range else '  '}")
        if in_range:
            results.append((name, val, mod71))
    print()
    
    # ========== ANGLE 135°-180°: ROTATIONS & SHIFTS ==========
    print("🟠 ANGLE 135°-180°: ROTATIONS & SHIFTS")
    print("-" * 80)
    
    # Bit rotations
    for shift in [8, 16, 32, 64, 128]:
        left = ((value << shift) | (value >> (256 - shift))) & ((1 << 256) - 1)
        right = ((value >> shift) | (value << (256 - shift))) & ((1 << 256) - 1)
        
        mod71_l = left % 71
        mod71_r = right % 71
        in_range_l = PUZZLE_71_START <= left <= PUZZLE_71_END
        in_range_r = PUZZLE_71_START <= right <= PUZZLE_71_END
        
        print(f"   ROL-{shift:3d}:          mod 71 = {mod71_l:3d}  {'🎯' if in_range_l else '  '}")
        print(f"   ROR-{shift:3d}:          mod 71 = {mod71_r:3d}  {'🎯' if in_range_r else '  '}")
        
        if in_range_l:
            results.append((f"ROL-{shift}", left, mod71_l))
        if in_range_r:
            results.append((f"ROR-{shift}", right, mod71_r))
    print()
    
    # ========== ANGLE 180°-225°: INVERSE SPECTRAL ==========
    print("🔴 ANGLE 180°-225°: INVERSE SPECTRAL")
    print("-" * 80)
    
    # Modular inverse
    def mod_inv(a, m):
        def egcd(a, b):
            if a == 0: return b, 0, 1
            gcd, x1, y1 = egcd(b % a, a)
            return gcd, y1 - (b // a) * x1, x1
        gcd, x, _ = egcd(a % m, m)
        return (x % m + m) % m if gcd == 1 else None
    
    inv_curve = mod_inv(value, CURVE_ORDER)
    if inv_curve:
        mod71 = inv_curve % 71
        in_range = PUZZLE_71_START <= inv_curve <= PUZZLE_71_END
        print(f"   value^-1 mod n:      mod 71 = {mod71:3d}  {'🎯' if in_range else '  '}")
        if in_range:
            results.append(("inv_curve", inv_curve, mod71))
    
    # Bitwise NOT
    bitwise_not = ((1 << 256) - 1) ^ value
    mod71 = bitwise_not % 71
    in_range = PUZZLE_71_START <= bitwise_not <= PUZZLE_71_END
    print(f"   ~value:              mod 71 = {mod71:3d}  {'🎯' if in_range else '  '}")
    if in_range:
        results.append(("bitwise_not", bitwise_not, mod71))
    print()
    
    # ========== ANGLE 225°-270°: POLYNOMIAL COMBINATIONS ==========
    print("🟣 ANGLE 225°-270°: POLYNOMIAL SPECTRAL")
    print("-" * 80)
    
    poly_ops = [
        ("value² mod n", (value * value) % CURVE_ORDER),
        ("value³ mod n", (value * value * value) % CURVE_ORDER),
        ("R² + S² mod n", ((sig_r**2) + (sig_s**2)) % CURVE_ORDER),
        ("(R+S)² mod n", ((sig_r + sig_s)**2) % CURVE_ORDER),
        ("value×R + S mod n", ((value * sig_r) + sig_s) % CURVE_ORDER),
        ("value×S + R mod n", ((value * sig_s) + sig_r) % CURVE_ORDER),
    ]
    
    for name, val in poly_ops:
        mod71 = val % 71
        in_range = PUZZLE_71_START <= val <= PUZZLE_71_END
        print(f"   {name:20s} mod 71 = {mod71:3d}  {'🎯' if in_range else '  '}")
        if in_range:
            results.append((name, val, mod71))
    print()
    
    # ========== ANGLE 270°-315°: MODULAR PATTERNS ==========
    print("🟤 ANGLE 270°-315°: MODULAR HARMONIC ANALYSIS")
    print("-" * 80)
    
    harmonics = [71, 42, 8, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    print("   Value modular fingerprint:")
    fingerprint = [value % h for h in harmonics]
    print(f"   {fingerprint}")
    print()
    
    # Check if patterns match
    r_finger = [sig_r % h for h in harmonics]
    s_finger = [sig_s % h for h in harmonics]
    print(f"   R fingerprint: {r_finger}")
    print(f"   S fingerprint: {s_finger}")
    print()
    
    # ========== ANGLE 315°-360°: COMPOSITE OPERATIONS ==========
    print("⚪ ANGLE 315°-360°: COMPOSITE SPECTRAL")
    print("-" * 80)
    
    composite = [
        ("(R⊕S) + value", (sig_r ^ sig_s) + value),
        ("(R+S) ⊕ value", ((sig_r + sig_s) % (2**256)) ^ value),
        ("R⊕value + S", (sig_r ^ value) + sig_s),
        ("(R×value) ⊕ S", ((sig_r * value) % CURVE_ORDER) ^ sig_s),
        ("R + (S⊕value)", sig_r + (sig_s ^ value)),
        ("(value²)⊕(R+S)", ((value * value) % CURVE_ORDER) ^ ((sig_r + sig_s) % CURVE_ORDER)),
    ]
    
    for name, val in composite:
        val = val % (2**256)
        mod71 = val % 71
        in_range = PUZZLE_71_START <= val <= PUZZLE_71_END
        print(f"   {name:20s} mod 71 = {mod71:3d}  {'🎯' if in_range else '  '}")
        if in_range:
            results.append((name, val, mod71))
    print()
    
    return results

def main():
    print("🌈 360° SPECTRAL ARRAY ANALYZER")
    print("=" * 80)
    
    # Input values
    bottom_string = "5b1c60b9e525ff756acca60972374422cfb52a736b9145"
    value = int(bottom_string, 16)
    
    sig_r = 0x61d383f74bacc73e5df7f8c3f780c3cf1485c78d07313651e1af6a2f67862897
    sig_s = 0x50eb836bffc9c2c3aa32746672faf3fe2cf8989e218fc617fc58fee14640622f
    pubkey_x = 0x2bccd43333d2ef5c805b1c60b9e525ff756acca60972374422cfb52a736b9145
    
    print(f"📝 Analyzing: {bottom_string}")
    print(f"   Decimal: {value}")
    print()
    
    # Run spectral analysis
    results = spectral_analysis_360(value, sig_r, sig_s, pubkey_x)
    
    # Summary
    print("=" * 80)
    print("🎯 SPECTRAL SCAN COMPLETE")
    print("=" * 80)
    
    if results:
        print(f"✅ Found {len(results)} value(s) in Puzzle 71 range!")
        print()
        for name, val, mod71 in results:
            print(f"🏆 {name}")
            print(f"   Hex: {val:064x}")
            print(f"   Dec: {val}")
            print(f"   mod 71 = {mod71}")
            print()
    else:
        print("❌ No values in Puzzle 71 range detected")
        print("   All 360° angles analyzed")
    
    print("=" * 80)

if __name__ == "__main__":
    main()
