#!/usr/bin/env python3
"""
Wallet UTXO Finder - Find your UTXOs for Bitcoin transactions
"""

from utxo_scanner import UTXOScanner
import json

def find_your_utxos():
    """Guide user to find their UTXOs"""
    
    print("💰 FIND YOUR BITCOIN UTXOs")
    print("=" * 50)
    print()
    print("🔑 I need information about wallets YOU CONTROL to find usable UTXOs.")
    print("   (Cannot use random addresses - you need the private keys!)")
    print()
    print("📋 OPTION 1: Provide Your Bitcoin Addresses")
    print("   If you have specific Bitcoin addresses with funds:")
    print("   - Legacy: 1ABC... (P2PKH)")
    print("   - SegWit: 3ABC... or bc1q... (P2SH-P2WPKH/P2WPKH)")
    print("   - Taproot: bc1p... (P2TR)")
    print()
    print("📋 OPTION 2: Provide Your Wallet Details")
    print("   - Extended Public Key (xpub/ypub/zpub)")
    print("   - Wallet descriptor")
    print("   - Seed phrase (if you trust this environment)")
    print()
    print("📋 OPTION 3: Manual Input")
    print("   - Specific TXID:VOUT pairs you want to spend")
    print("   - Amounts and addresses for those outputs")
    print()
    
    # Option to scan provided addresses
    print("🚀 QUICK START: Provide addresses to scan")
    print("   Edit this function with your addresses, then run:")
    print("   python3 wallet_utxo_finder.py")
    print()
    
    return scan_example_addresses()

def scan_example_addresses():
    """Example of how to scan your own addresses"""
    
    scanner = UTXOScanner()
    
    # REPLACE THESE WITH YOUR ACTUAL ADDRESSES
    your_addresses = [
        # "1YourBitcoinAddressHere...",           # Add your P2PKH address
        # "3YourSegWitAddressHere...",            # Add your P2SH-P2WPKH address  
        # "bc1qyourNativeSegWitAddressHere...",   # Add your P2WPKH address
        # "bc1pyourTaprootAddressHere...",        # Add your P2TR address
    ]
    
    if not your_addresses:
        print("❌ No addresses provided!")
        print("📝 Edit wallet_utxo_finder.py and add your Bitcoin addresses")
        print("   Then run: python3 wallet_utxo_finder.py")
        return None
    
    print(f"🔍 Scanning {len(your_addresses)} of YOUR addresses...")
    
    # Find all UTXOs (any size, 1+ confirmations)
    utxos = scanner.scan_multiple_addresses(your_addresses, min_confirmations=1)
    
    if utxos:
        print("\n" + scanner.generate_utxo_summary(utxos))
        
        # Select best UTXOs for large transaction
        large_utxos = [utxo for utxo in utxos if utxo['value'] >= 100000000]  # >= 1 BTC
        
        if large_utxos:
            print(f"\n🎯 LARGE UTXOs (>= 1 BTC) READY FOR TRANSACTION:")
            print("=" * 60)
            
            for utxo in large_utxos[:10]:  # Top 10
                btc_value = utxo['value'] / 100000000
                print(f"💎 {btc_value:12.8f} BTC")
                print(f"   TXID: {utxo['txid']}")
                print(f"   VOUT: {utxo['vout']}")
                print(f"   Address: {utxo['address']}")
                print(f"   Confirmations: {utxo['confirmations']}")
                print()
            
            # Export for transaction builder
            export_data = {
                'timestamp': time.time(),
                'total_utxos': len(utxos),
                'large_utxos': len(large_utxos),
                'utxos': large_utxos[:5]  # Top 5 for transaction
            }
            
            with open('available_utxos.json', 'w') as f:
                json.dump(export_data, f, indent=2)
            
            print(f"✅ Exported {len(large_utxos)} large UTXOs to available_utxos.json")
            return large_utxos
        
        else:
            print(f"\n⚠️  Found {len(utxos)} UTXOs but none >= 1 BTC")
            print("   Consider combining smaller UTXOs or adjusting requirements")
    
    else:
        print("\n❌ No UTXOs found in provided addresses")
        print("💡 Double-check your addresses have confirmed transactions")
    
    return None

def scan_from_xpub(xpub, account_type="p2wpkh", gap_limit=20):
    """Scan UTXOs from extended public key (advanced)"""
    print(f"🔑 Scanning from xpub: {xpub[:20]}...")
    print(f"📊 Account type: {account_type}, Gap limit: {gap_limit}")
    
    # This would require implementing HD wallet derivation
    # For now, prompt user to use a wallet tool
    
    print("⚠️  HD wallet derivation not implemented yet")
    print("💡 Use your wallet software to:")
    print("   1. Export receiving addresses")
    print("   2. Add them to scan_example_addresses()")
    print("   3. Run the scanner")
    
    return None

if __name__ == "__main__":
    import time
    find_your_utxos()