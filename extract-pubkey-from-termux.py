
#!/usr/bin/env python3
"""
Extract public key from Termux hex strings and verify against Puzzle 71
"""

import hashlib

PUZZLE_71_HASH160 = "f6f5431d25bbf7b12e8add9af5e3475c44a0a5b8"
PUZZLE_71_ADDRESS = "1PWo3JeB9jrGwfHDNpdGK54CRas7fsVzXU"

# All possible public key candidates from the strings
CANDIDATES = [
    # Last string starts with pubkey-like pattern
    "022bccd43333d2ef5c805b1c60b9e525ff756acca60972374422cfb52a736b9145",
    
    # Try combining parts
    "f3fe2cf8989e218fc617fc58fee1446062f0121022bccd43333d2ef5c805b1c60b9e525ff756acca60972374422cfb52a736b9145",
]

print("🔑 PUBLIC KEY EXTRACTION FROM TERMUX")
print("=" * 80)
print(f"📍 Target Address: {PUZZLE_71_ADDRESS}")
print(f"📍 Target Hash160: {PUZZLE_71_HASH160}")
print()

for i, candidate in enumerate(CANDIDATES, 1):
    print(f"\n{'=' * 80}")
    print(f"🧪 CANDIDATE #{i}")
    print(f"{'=' * 80}")
    print(f"Hex: {candidate}")
    print(f"Length: {len(candidate)//2} bytes ({len(candidate)} hex chars)")
    
    # Check if it's valid pubkey length
    if len(candidate) == 66:  # Compressed
        print("✅ Valid compressed pubkey length (33 bytes)")
    elif len(candidate) == 130:  # Uncompressed
        print("✅ Valid uncompressed pubkey length (65 bytes)")
    else:
        print(f"⚠️  Unusual length - not standard pubkey format")
    
    # Check prefix
    if candidate.startswith('02') or candidate.startswith('03'):
        print("✅ Valid compressed pubkey prefix")
    elif candidate.startswith('04'):
        print("✅ Valid uncompressed pubkey prefix")
    
    # Try to derive address
    try:
        pubkey_bytes = bytes.fromhex(candidate)
        sha256 = hashlib.sha256(pubkey_bytes).digest()
        hash160 = hashlib.new('ripemd160', sha256).hexdigest()
        
        print(f"\n🔍 DERIVED HASH160:")
        print(f"   Computed: {hash160}")
        print(f"   Target:   {PUZZLE_71_HASH160}")
        
        if hash160 == PUZZLE_71_HASH160:
            print(f"\n🎉🎉🎉 MATCH FOUND! 🎉🎉🎉")
            print(f"This is the correct public key for Puzzle 71!")
            print(f"Public Key: {candidate}")
        else:
            print(f"   ❌ No match")
            
            # Show difference
            diff_count = sum(1 for a, b in zip(hash160, PUZZLE_71_HASH160) if a != b)
            print(f"   Character differences: {diff_count}/40")
            
    except Exception as e:
        print(f"❌ Error deriving address: {e}")

print("\n" + "=" * 80)
print("✅ Extraction complete")
print("=" * 80)
