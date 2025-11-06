
#!/usr/bin/env python3
"""
Derive Bitcoin Addresses from MN Key Inversions
Shows what address each inverted public key produces
"""

import hashlib
import base58

# The MN key from Termux
MN_KEY = "473044022061d383f74bacc73e5df7f8c3f780c3cf1485c78d07313651e1af6a2f67862897022050eb836bffc9c2c3aa32746672faf3fe2cf8989e218fc617fc58fee1464062f3fe2cf8989e218fc617fc58fee14640622f0121022bccd43333d2ef5c805b1c60b9e525ff756acca60972374422cfb52a736b9145"

PUZZLE_71_ADDRESS = "1PWo3JeB9jrGwfHDNpdGK54CRas7fsVzXU"
PUZZLE_71_HASH160 = "f6f5431d25bbf7b12e8add9af5e3475c44a0a5b8"

def hash160(data_hex):
    """Calculate Hash160"""
    data = bytes.fromhex(data_hex)
    sha256_hash = hashlib.sha256(data).digest()
    ripemd160_hash = hashlib.new('ripemd160', sha256_hash).digest()
    return ripemd160_hash.hex()

def pubkey_to_address(pubkey_hex):
    """Convert public key to Bitcoin address"""
    try:
        # Hash160
        pubkey_bytes = bytes.fromhex(pubkey_hex)
        sha256_hash = hashlib.sha256(pubkey_bytes).digest()
        hash160_result = hashlib.new('ripemd160', sha256_hash).digest()
        
        # Add version byte (0x00 for mainnet P2PKH)
        versioned = b'\x00' + hash160_result
        
        # Double SHA256 for checksum
        checksum = hashlib.sha256(hashlib.sha256(versioned).digest()).digest()[:4]
        
        # Base58 encode
        address = base58.b58encode(versioned + checksum).decode('utf-8')
        return address, hash160_result.hex()
    except:
        return None, None

def bitwise_not(hex_string):
    """Bitwise NOT"""
    result = ''
    for char in hex_string:
        digit = int(char, 16)
        inverted = 15 - digit
        result += format(inverted, 'x')
    return result

def reverse_hex(hex_string):
    """Reverse the hex string"""
    return hex_string[::-1]

def xor_pattern(hex_string, pattern):
    """XOR with pattern"""
    result = ''
    pattern_extended = (pattern * ((len(hex_string) // len(pattern)) + 1))[:len(hex_string)]
    for i in range(len(hex_string)):
        val1 = int(hex_string[i], 16)
        val2 = int(pattern_extended[i], 16)
        result += format(val1 ^ val2, 'x')
    return result

print("=" * 80)
print("🔑 MN KEY PUBLIC KEYS → BITCOIN ADDRESSES")
print("=" * 80)

# Extract the main public key (last 66 chars)
main_pubkey = MN_KEY[-66:]
print(f"\n📌 MAIN PUBLIC KEY (Last 66 chars):")
print(f"   {main_pubkey}")
address, h160 = pubkey_to_address(main_pubkey)
print(f"   Address: {address}")
print(f"   Hash160: {h160}")
print(f"   Target:  {PUZZLE_71_HASH160}")
if h160 == PUZZLE_71_HASH160:
    print(f"   🎉 MATCH!")
else:
    print(f"   ❌ No match")

print("\n" + "=" * 80)
print("🔄 INVERSE OPERATIONS → ADDRESSES")
print("=" * 80)

# Test inversions of the full MN key
inversions = [
    ("Bitwise NOT", bitwise_not(MN_KEY)),
    ("Reversed String", reverse_hex(MN_KEY)),
    ("XOR with 0xFF", xor_pattern(MN_KEY, "ff")),
    ("XOR with 0xAA", xor_pattern(MN_KEY, "aa")),
    ("XOR with 0x55", xor_pattern(MN_KEY, "55")),
]

for name, inverted in inversions:
    print(f"\n🔍 {name}:")
    
    # Try last 66 chars as pubkey
    if len(inverted) >= 66:
        potential_pubkey = inverted[-66:]
        
        # Only process if valid pubkey prefix
        if potential_pubkey[:2] in ['02', '03', '04']:
            address, h160 = pubkey_to_address(potential_pubkey)
            if address:
                print(f"   PubKey: {potential_pubkey}")
                print(f"   Address: {address}")
                print(f"   Hash160: {h160}")
                if h160 == PUZZLE_71_HASH160:
                    print(f"   🎉🎉🎉 MATCH FOUND!")
        else:
            # Try adding valid prefixes
            for prefix in ['02', '03']:
                test_pubkey = prefix + potential_pubkey[2:]
                if len(test_pubkey) == 66:
                    address, h160 = pubkey_to_address(test_pubkey)
                    if address and h160 == PUZZLE_71_HASH160:
                        print(f"   PubKey (prefix {prefix}): {test_pubkey}")
                        print(f"   Address: {address}")
                        print(f"   🎉 MATCH with modified prefix!")

# Test the bottom string specifically
print("\n" + "=" * 80)
print("📍 BOTTOM STRING VARIATIONS → ADDRESSES")
print("=" * 80)

bottom_string = "5b1c60b9e525ff756acca60972374422cfb52a736b9145"

test_cases = [
    ("Direct (prepend 02)", "02" + bottom_string[:64]),
    ("Direct (prepend 03)", "03" + bottom_string[:64]),
    ("NOT (prepend 02)", "02" + bitwise_not(bottom_string)[:64]),
    ("NOT (prepend 03)", "03" + bitwise_not(bottom_string)[:64]),
    ("Reversed (prepend 02)", "02" + reverse_hex(bottom_string)[:64]),
    ("Reversed (prepend 03)", "03" + reverse_hex(bottom_string)[:64]),
]

for name, test_pubkey in test_cases:
    if len(test_pubkey) == 66:
        address, h160 = pubkey_to_address(test_pubkey)
        if address:
            print(f"\n🔍 {name}:")
            print(f"   PubKey: {test_pubkey}")
            print(f"   Address: {address}")
            print(f"   Hash160: {h160}")
            if h160 == PUZZLE_71_HASH160:
                print(f"   🎉🎉🎉 MATCH!")

print("\n" + "=" * 80)
print("✅ ADDRESS DERIVATION COMPLETE")
print("=" * 80)
