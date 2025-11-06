
#!/usr/bin/env python3
"""
Check MN Key (Master Node key from Termux) and its Inverse
Analyzes the hex string from the Termux screenshot
"""

import hashlib

# From the Termux screenshot - the long hex string
MN_KEY = "473044022061d383f74bacc73e5df7f8c3f780c3cf1485c78d07313651e1af6a2f67862897022050eb836bffc9c2c3aa32746672faf3fe2cf8989e218fc617fc58fee1464062f3fe2cf8989e218fc617fc58fee14640622f0121022bccd43333d2ef5c805b1c60b9e525ff756acca60972374422cfb52a736b9145"

PUZZLE_71_HASH160 = "f6f5431d25bbf7b12e8add9af5e3475c44a0a5b8"
PUZZLE_71_ADDRESS = "1PWo3JeB9jrGwfHDNpdGK54CRas7fsVzXU"

def hash160(data_hex):
    """Calculate Hash160 (RIPEMD160(SHA256(data)))"""
    data = bytes.fromhex(data_hex)
    sha256_hash = hashlib.sha256(data).digest()
    ripemd160_hash = hashlib.new('ripemd160', sha256_hash).digest()
    return ripemd160_hash.hex()

def bitwise_not(hex_string):
    """Bitwise NOT (inverse) - flip all bits"""
    result = ''
    for char in hex_string:
        digit = int(char, 16)
        inverted = 15 - digit
        result += format(inverted, 'x')
    return result

def twos_complement(hex_string):
    """Two's complement (NOT + 1)"""
    # Convert to int, invert, add 1
    num = int(hex_string, 16)
    bit_length = len(hex_string) * 4
    mask = (1 << bit_length) - 1
    inverted = (~num) & mask
    twos_comp = (inverted + 1) & mask
    return format(twos_comp, f'0{len(hex_string)}x')

def reverse_hex(hex_string):
    """Reverse the hex string"""
    return hex_string[::-1]

def reverse_bytes(hex_string):
    """Reverse byte order"""
    result = ''
    for i in range(len(hex_string) - 2, -1, -2):
        result += hex_string[i:i+2]
    return result

def xor_with_pattern(hex_string, pattern):
    """XOR with repeating pattern"""
    result = ''
    pattern_extended = (pattern * ((len(hex_string) // len(pattern)) + 1))[:len(hex_string)]
    for i in range(len(hex_string)):
        val1 = int(hex_string[i], 16)
        val2 = int(pattern_extended[i], 16)
        result += format(val1 ^ val2, 'x')
    return result

print("=" * 80)
print("🔑 MN KEY (MASTER NODE KEY) ANALYSIS")
print("=" * 80)
print(f"\n📝 Full MN Key: {MN_KEY}")
print(f"   Length: {len(MN_KEY)} hex chars ({len(MN_KEY)//2} bytes)")
print()

# Extract potential public key from the end (last 66 chars = compressed pubkey)
if len(MN_KEY) >= 66:
    potential_pubkey = MN_KEY[-66:]
    print(f"🔑 Potential Public Key (last 66 chars):")
    print(f"   {potential_pubkey}")
    
    if potential_pubkey.startswith('02') or potential_pubkey.startswith('03'):
        print("   ✅ Valid compressed pubkey prefix!")
        pubkey_hash = hash160(potential_pubkey)
        print(f"\n   Hash160: {pubkey_hash}")
        print(f"   Target:  {PUZZLE_71_HASH160}")
        if pubkey_hash == PUZZLE_71_HASH160:
            print("   🎉🎉🎉 MATCH FOUND! This is Puzzle 71's public key!")
        else:
            diff = sum(1 for a, b in zip(pubkey_hash, PUZZLE_71_HASH160) if a != b)
            print(f"   ❌ No match ({diff}/40 chars different)")
print()

# Try different segments as potential keys
segments = [
    ("First 64 chars", MN_KEY[:64] if len(MN_KEY) >= 64 else MN_KEY),
    ("Middle 64 chars", MN_KEY[64:128] if len(MN_KEY) >= 128 else ""),
    ("Last 64 chars", MN_KEY[-64:] if len(MN_KEY) >= 64 else ""),
]

print("=" * 80)
print("🔍 TESTING KEY SEGMENTS")
print("=" * 80)

for name, segment in segments:
    if not segment or len(segment) < 40:
        continue
    
    print(f"\n{name}:")
    print(f"   {segment}")
    
    # Try as direct hash160
    if len(segment) == 40:
        print(f"   Testing as Hash160...")
        if segment.lower() == PUZZLE_71_HASH160:
            print(f"   🎉 EXACT MATCH!")
    
    # Try as pubkey
    if len(segment) == 66 and segment[:2] in ['02', '03', '04']:
        h160 = hash160(segment)
        print(f"   Hash160: {h160}")
        if h160 == PUZZLE_71_HASH160:
            print(f"   🎉 MATCH!")

print()
print("=" * 80)
print("🔄 INVERSE OPERATIONS ON FULL MN KEY")
print("=" * 80)

inversions = [
    ("Bitwise NOT", bitwise_not(MN_KEY)),
    ("Two's Complement", twos_complement(MN_KEY)),
    ("Reversed String", reverse_hex(MN_KEY)),
    ("Reversed Bytes", reverse_bytes(MN_KEY)),
    ("XOR with 0xAA", xor_with_pattern(MN_KEY, "aa")),
    ("XOR with 0x55", xor_with_pattern(MN_KEY, "55")),
    ("XOR with 0xFF", xor_with_pattern(MN_KEY, "ff")),
]

for name, inverted in inversions:
    print(f"\n{name}:")
    print(f"   {inverted[:80]}...")
    
    # Check if last 66 chars form a valid pubkey
    if len(inverted) >= 66:
        potential_pubkey = inverted[-66:]
        if potential_pubkey[:2] in ['02', '03', '04']:
            print(f"   Found potential pubkey: {potential_pubkey}")
            h160 = hash160(potential_pubkey)
            print(f"   Hash160: {h160}")
            if h160 == PUZZLE_71_HASH160:
                print(f"   🎉🎉🎉 MATCH FOUND!")

print()
print("=" * 80)
print("🎯 SPECIFIC INVERSE TESTS")
print("=" * 80)

# Test the bottom string specifically
bottom_string = "5b1c60b9e525ff756acca60972374422cfb52a736b9145"
print(f"\nBottom string from screenshot:")
print(f"   {bottom_string}")

bottom_inversions = [
    ("NOT", bitwise_not(bottom_string)),
    ("Two's Comp", twos_complement(bottom_string)),
    ("Reversed", reverse_hex(bottom_string)),
]

for name, inv in bottom_inversions:
    print(f"\n{name}: {inv}")
    
    # Try prepending 02/03 to make it a pubkey
    for prefix in ['02', '03']:
        if len(inv) <= 64:
            test_pubkey = prefix + inv.ljust(64, '0')
            h160 = hash160(test_pubkey)
            if h160 == PUZZLE_71_HASH160:
                print(f"   🎉 MATCH with prefix {prefix}!")
                print(f"   Public Key: {test_pubkey}")

print()
print("=" * 80)
print("✅ ANALYSIS COMPLETE")
print("=" * 80)
