#!/usr/bin/env python3
"""
PRIVATE KEY EXTRACTOR
Attempts to derive/find private key from signature + public key data
"""

import sys
import hashlib
import base58

def pubkey_to_address(pubkey_hex):
    """Convert compressed public key to Bitcoin address"""
    pubkey = bytes.fromhex(pubkey_hex)
    
    # SHA256
    sha256_hash = hashlib.sha256(pubkey).digest()
    
    # RIPEMD160
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(sha256_hash)
    hash160 = ripemd160.digest()
    
    # Add version byte (0x00 for mainnet P2PKH)
    versioned_payload = b'\x00' + hash160
    
    # Double SHA256 for checksum
    checksum = hashlib.sha256(hashlib.sha256(versioned_payload).digest()).digest()[:4]
    
    # Final address
    address_bytes = versioned_payload + checksum
    address = base58.b58encode(address_bytes).decode('utf-8')
    
    return address

def main():
    print("🔐 PRIVATE KEY EXTRACTION ATTEMPT")
    print("=" * 80)
    
    # From witness script analysis
    signature_r = 0x61d383f74bacc73e5df7f8c3f780c3cf1485c78d07313651e1af6a2f67862897
    signature_s = 0x50eb836bffc9c2c3aa32746672faf3fe2cf8989e218fc617fc58fee14640622f
    pubkey_hex = "022bccd43333d2ef5c805b1c60b9e525ff756acca60972374422cfb52a736b9145"
    pubkey_x = 0x2bccd43333d2ef5c805b1c60b9e525ff756acca60972374422cfb52a736b9145
    
    print(f"📝 Public Key: {pubkey_hex}")
    print()
    
    # Generate Bitcoin address
    address = pubkey_to_address(pubkey_hex)
    print(f"📍 Bitcoin Address: {address}")
    print()
    
    # Check if it's Puzzle 71
    puzzle_71_address = "1PWo3JeB9jrGwfHDNpdGK54CRas7fsVzXU"
    
    if address == puzzle_71_address:
        print("🎉" * 40)
        print("🏆 THIS IS PUZZLE 71 ADDRESS!")
        print("🎉" * 40)
    else:
        print(f"❌ Not Puzzle 71 (target: {puzzle_71_address})")
    
    print()
    print("=" * 80)
    print("🔍 PRIVATE KEY RECOVERY ANALYSIS:")
    print("=" * 80)
    print()
    print("⚠️  REALITY CHECK:")
    print("   • Private key CANNOT be derived from public key alone")
    print("   • That's the entire security of Bitcoin!")
    print("   • Signature + pubkey does NOT reveal private key")
    print()
    print("🛡️  Only vulnerabilities that could work:")
    print("   1. Nonce reuse (same k in two different signatures)")
    print("   2. Weak random number generator")
    print("   3. Side-channel attacks (not applicable here)")
    print("   4. Brute force (only for weak keys)")
    print()
    print("📊 For this specific transaction:")
    print(f"   • R value: {signature_r}")
    print(f"   • S value: {signature_s}")
    print(f"   • Public key X: {pubkey_x}")
    print()
    print("🎯 CONCLUSION:")
    print("   Without another signature using the SAME nonce (k),")
    print("   or additional vulnerability, private key cannot be recovered.")
    print()
    print("=" * 80)
    print(f"✅ Address for this pubkey: {address}")
    print("=" * 80)

if __name__ == "__main__":
    main()
