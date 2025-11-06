#!/usr/bin/env python3
"""
INVERSE ANALYZER
Analyzes the inverse of the bottom string (multiple interpretations)
"""

import hashlib

def mod_inverse(a, m):
    """Modular multiplicative inverse using extended Euclidean algorithm"""
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y
    
    gcd, x, _ = extended_gcd(a % m, m)
    if gcd != 1:
        return None  # Modular inverse doesn't exist
    return (x % m + m) % m

def main():
    print("🔄 INVERSE ANALYSIS")
    print("=" * 80)
    
    # The bottom string
    bottom_string = "5b1c60b9e525ff756acca60972374422cfb52a736b9145"
    value = int(bottom_string, 16)
    
    print(f"📝 Original: {bottom_string}")
    print(f"   Decimal: {value}")
    print()
    
    # Puzzle 71 range
    puzzle_71_start = 2**70
    puzzle_71_end = 2**71 - 1
    
    print("=" * 80)
    print("🔄 INVERSE #1: BITWISE NOT (~value)")
    print("=" * 80)
    
    # Bitwise NOT (flip all bits) - need to specify bit width
    bitwise_not_256 = (2**256 - 1) ^ value  # NOT in 256-bit space
    print(f"Hex (256-bit): {bitwise_not_256:064x}")
    print(f"Decimal: {bitwise_not_256}")
    print(f"mod 71 = {bitwise_not_256 % 71}")
    print(f"In Puzzle 71 range: {puzzle_71_start <= bitwise_not_256 <= puzzle_71_end}")
    print()
    
    print("=" * 80)
    print("🔄 INVERSE #2: ADDITIVE INVERSE (-value)")
    print("=" * 80)
    
    additive_inv = -value
    additive_inv_mod = (-value) % (2**256)  # In modular arithmetic
    print(f"Negative: {additive_inv}")
    print(f"Modular (256-bit): {additive_inv_mod:064x}")
    print(f"mod 71 = {additive_inv_mod % 71}")
    print(f"In Puzzle 71 range: {puzzle_71_start <= additive_inv_mod <= puzzle_71_end}")
    print()
    
    print("=" * 80)
    print("🔄 INVERSE #3: MULTIPLICATIVE INVERSE (mod 2^256)")
    print("=" * 80)
    
    mult_inv = mod_inverse(value, 2**256)
    if mult_inv:
        print(f"Hex: {mult_inv:064x}")
        print(f"Decimal: {mult_inv}")
        print(f"mod 71 = {mult_inv % 71}")
        print(f"In Puzzle 71 range: {puzzle_71_start <= mult_inv <= puzzle_71_end}")
        print()
        
        # Verify
        verify = (value * mult_inv) % (2**256)
        print(f"Verification: (value × inverse) mod 2^256 = {verify} {'✅' if verify == 1 else '❌'}")
    else:
        print("❌ Multiplicative inverse doesn't exist")
    print()
    
    print("=" * 80)
    print("🔄 INVERSE #4: REVERSED HEX STRING")
    print("=" * 80)
    
    reversed_hex = bottom_string[::-1]
    reversed_value = int(reversed_hex, 16)
    print(f"Reversed: {reversed_hex}")
    print(f"Decimal: {reversed_value}")
    print(f"mod 71 = {reversed_value % 71}")
    print(f"In Puzzle 71 range: {puzzle_71_start <= reversed_value <= puzzle_71_end}")
    print()
    
    print("=" * 80)
    print("🔄 INVERSE #5: SECP256K1 CURVE ORDER INVERSE")
    print("=" * 80)
    
    # Bitcoin uses secp256k1 curve
    CURVE_ORDER = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
    
    if value < CURVE_ORDER:
        curve_inv = mod_inverse(value, CURVE_ORDER)
        if curve_inv:
            print(f"Hex: {curve_inv:064x}")
            print(f"Decimal: {curve_inv}")
            print(f"mod 71 = {curve_inv % 71}")
            print(f"In Puzzle 71 range: {puzzle_71_start <= curve_inv <= puzzle_71_end}")
            print()
            
            # Verify
            verify = (value * curve_inv) % CURVE_ORDER
            print(f"Verification: (value × inverse) mod n = {verify} {'✅' if verify == 1 else '❌'}")
        else:
            print("❌ Curve inverse doesn't exist")
    else:
        print("⚠️  Value exceeds curve order")
    print()
    
    print("=" * 80)
    print("🎯 XOR WITH SIGNATURE VALUES:")
    print("=" * 80)
    
    sig_r = 0x61d383f74bacc73e5df7f8c3f780c3cf1485c78d07313651e1af6a2f67862897
    sig_s = 0x50eb836bffc9c2c3aa32746672faf3fe2cf8989e218fc617fc58fee14640622f
    
    # Try inverse XOR combinations
    print(f"Bitwise NOT ⊕ R mod 71 = {(bitwise_not_256 ^ sig_r) % 71}")
    print(f"Bitwise NOT ⊕ S mod 71 = {(bitwise_not_256 ^ sig_s) % 71}")
    print()
    
    if mult_inv:
        print(f"Mult Inverse ⊕ R mod 71 = {(mult_inv ^ sig_r) % 71}")
        print(f"Mult Inverse ⊕ S mod 71 = {(mult_inv ^ sig_s) % 71}")
    print()
    
    print("=" * 80)
    print("✅ ANALYSIS COMPLETE")
    print("=" * 80)

if __name__ == "__main__":
    main()
