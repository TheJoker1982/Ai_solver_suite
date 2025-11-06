
#!/usr/bin/env python3
"""
Analyze hex strings from Termux screenshot
Combined with correct Puzzle 71 hash160
"""

import hashlib

# Correct Puzzle 71 data
PUZZLE_71_ADDRESS = "1PWo3JeB9jrGwfHDNpdGK54CRas7fsVzXU"
PUZZLE_71_HASH160 = "f6f5431d25bbf7b12e8add9af5e3475c44a0a5b8"

# Hex strings from Termux screenshot
HEX_STRINGS = [
    "473044022061d383f74bacc73e5df7f8c3f780c3cf1485",
    "e78d07313651e1af6a2f6786289702205eb836bffc9c2c3aa327466727fa",
    "f3fe2cf8989e218fc617fc58fee1446062f0121022bccd43333d2ef5c80",
    "5b1c60b9e525ff756acca60972374422cfb52a736b9145"
]

# Try concatenating all strings
FULL_STRING = "".join(HEX_STRINGS)

print("🔍 TERMUX HEX STRING ANALYSIS")
print("=" * 80)
print(f"📍 Target: {PUZZLE_71_ADDRESS}")
print(f"📍 Hash160: {PUZZLE_71_HASH160}")
print()

print("📋 HEX STRINGS FROM SCREENSHOT:")
for i, s in enumerate(HEX_STRINGS, 1):
    print(f"   {i}. {s}")
    print(f"      Length: {len(s)//2} bytes")
print()

print("🔗 CONCATENATED STRING:")
print(f"   {FULL_STRING}")
print(f"   Total length: {len(FULL_STRING)//2} bytes ({len(FULL_STRING)} hex chars)")
print()

# Analyze each string
print("=" * 80)
print("🔬 INDIVIDUAL STRING ANALYSIS:")
print("=" * 80)

for i, hex_str in enumerate(HEX_STRINGS, 1):
    print(f"\n📊 STRING #{i}: {hex_str[:32]}...")
    
    try:
        value = int(hex_str, 16)
        print(f"   Decimal: {value}")
        print(f"   mod 71 = {value % 71}")
        print(f"   mod 42 = {value % 42}")
        print(f"   mod 8 = {value % 8}")
        
        # Check if it's a public key prefix
        if hex_str.startswith('02') or hex_str.startswith('03'):
            print(f"   ✅ COMPRESSED PUBLIC KEY PREFIX!")
        if hex_str.startswith('04'):
            print(f"   ✅ UNCOMPRESSED PUBLIC KEY PREFIX!")
            
        # Check if it matches known signature format (DER)
        if hex_str.startswith('30'):
            print(f"   ✅ DER SIGNATURE FORMAT!")
            
    except Exception as e:
        print(f"   ❌ Error: {e}")

# Try to find public key
print("\n" + "=" * 80)
print("🔑 PUBLIC KEY SEARCH:")
print("=" * 80)

# Look for 02/03 prefix (compressed pubkey is 33 bytes = 66 hex chars)
for hex_str in HEX_STRINGS:
    if hex_str.startswith('02') or hex_str.startswith('03'):
        if len(hex_str) == 66:
            print(f"\n✅ FOUND COMPRESSED PUBLIC KEY:")
            print(f"   {hex_str}")
            
            # Derive address from this pubkey
            try:
                import hashlib
                pubkey_bytes = bytes.fromhex(hex_str)
                sha256 = hashlib.sha256(pubkey_bytes).digest()
                ripemd160 = hashlib.new('ripemd160', sha256).hexdigest()
                
                print(f"   Hash160: {ripemd160}")
                print(f"   Target:  {PUZZLE_71_HASH160}")
                print(f"   Match: {'✅ YES!' if ripemd160 == PUZZLE_71_HASH160 else '❌ NO'}")
            except Exception as e:
                print(f"   Error deriving address: {e}")

# Check for known signature values
print("\n" + "=" * 80)
print("🔍 KNOWN SIGNATURE COMPONENT CHECK:")
print("=" * 80)

# Known R and S from witness data
SIG_R = 0x0e1aee72f4218cec033a08b2744e4d1d3481fba78ff504f24d2465086dfc901c
SIG_S = 0x5fa4a4bc4e88565724458b755036b231527c4e8e587b90d3934aa6c779ebda17

for i, hex_str in enumerate(HEX_STRINGS, 1):
    try:
        value = int(hex_str, 16)
        
        if value == SIG_R:
            print(f"✅ STRING #{i} MATCHES SIGNATURE R!")
        if value == SIG_S:
            print(f"✅ STRING #{i} MATCHES SIGNATURE S!")
            
        # Check partial matches
        if hex(SIG_R)[2:].startswith(hex_str) or hex_str in hex(SIG_R)[2:]:
            print(f"⚠️  STRING #{i} PARTIAL MATCH with R")
        if hex(SIG_S)[2:].startswith(hex_str) or hex_str in hex(SIG_S)[2:]:
            print(f"⚠️  STRING #{i} PARTIAL MATCH with S")
    except:
        pass

# XOR analysis with hash160
print("\n" + "=" * 80)
print("🧪 XOR WITH PUZZLE 71 HASH160:")
print("=" * 80)

hash160_int = int(PUZZLE_71_HASH160, 16)

for i, hex_str in enumerate(HEX_STRINGS, 1):
    try:
        # Pad to same length as hash160 (40 hex chars = 20 bytes)
        if len(hex_str) <= 40:
            padded = hex_str.zfill(40)
            value = int(padded, 16)
            xor_result = value ^ hash160_int
            
            print(f"\nSTRING #{i} ⊕ Hash160:")
            print(f"   Result: {xor_result:040x}")
            print(f"   Leading zeros: {len(f'{xor_result:040x}') - len(f'{xor_result:040x}'.lstrip('0'))}")
    except:
        pass

print("\n" + "=" * 80)
print("✅ Analysis complete!")
print("=" * 80)
