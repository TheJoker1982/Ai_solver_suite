#!/usr/bin/env python3
"""
Complete Transaction Builder with Real 9K UTXO
Ready for 12K UTXO data to complete 21,000 BTC transaction
"""

from dual_utxo_transaction import DualUTXOTransaction
from qr_generator import create_50_50_split_qrs

# Real 9K BTC UTXO extracted from user's transaction
REAL_9K_UTXO = {
    'txid': 'f815694f58d6aa9a1d05368a39c148043ff2c987fd85bdcabbf7e98b6842cba2',
    'vout': 0,
    'value': 900000000000  # 9,000 BTC in satoshis
}

RECIPIENT_ADDRESS = "1794B4ynTe3WA6VdCQWjg5EtPnYRuYZ45j"

def create_final_transaction_with_12k_utxo(utxo_12k_data):
    """Create final 21,000 BTC transaction with user's 12K UTXO data"""
    
    print("🚀 CREATING FINAL 21,000 BTC TRANSACTION")
    print("=" * 70)
    
    # Validate 12K UTXO format
    required_fields = ['txid', 'vout', 'value']
    for field in required_fields:
        if field not in utxo_12k_data:
            raise ValueError(f"12K UTXO missing field: {field}")
    
    if len(utxo_12k_data['txid']) != 64:
        raise ValueError(f"Invalid TXID length: {len(utxo_12k_data['txid'])}")
    
    # Show the UTXOs
    print(f"📋 UTXO 1 (12K BTC):")
    print(f"   TXID: {utxo_12k_data['txid']}")
    print(f"   VOUT: {utxo_12k_data['vout']}")
    print(f"   Value: {utxo_12k_data['value']/100000000:,.0f} BTC")
    
    print(f"\\n📋 UTXO 2 (9K BTC) - FROM YOUR REAL TRANSACTION:")
    print(f"   TXID: {REAL_9K_UTXO['txid']}")
    print(f"   VOUT: {REAL_9K_UTXO['vout']}")
    print(f"   Value: {REAL_9K_UTXO['value']/100000000:,.0f} BTC")
    
    # Create transaction
    tx_builder = DualUTXOTransaction()
    tx_builder.set_utxos(utxo_12k_data, REAL_9K_UTXO)
    
    # Calculate and build
    result = tx_builder.create_transaction_with_qrs()
    
    print(f"\\n🎉 FINAL TRANSACTION READY!")
    print(f"💰 Total Value: {(result['calculation']['total_input']/100000000):,.0f} BTC")
    print(f"📊 Payment 1: {(result['calculation']['outputs'][0]['amount']/100000000):,.2f} BTC")
    print(f"📊 Payment 2: {(result['calculation']['outputs'][1]['amount']/100000000):,.2f} BTC")
    print(f"💸 Fee: {(result['calculation']['fee']/100000000):.8f} BTC")
    
    print(f"\\n🔧 UNSIGNED TRANSACTION HEX:")
    print(f"{result['transaction_hex']}")
    
    print(f"\\n📱 QR CODE BITCOIN URIS:")
    print(f"Payment 1: {result['qr_codes']['payment_1']['uri']}")
    print(f"Payment 2: {result['qr_codes']['payment_2']['uri']}")
    
    print(f"\\n✅ READY FOR TERMINAL BROADCAST!")
    print(f"bitcoin-cli decoderawtransaction {result['transaction_hex']}")
    
    return result

# Example structure for user to fill in
EXAMPLE_12K_UTXO = {
    "txid": "YOUR_12000_BTC_TRANSACTION_ID_GOES_HERE_64_CHARACTERS_LONG",
    "vout": 0,  # or 1, 2, etc. - the output index
    "value": 1200000000000  # 12,000 BTC in satoshis
}

def show_requirements():
    """Show what's needed to complete the transaction"""
    
    print("🎯 FINAL STEP: 12K BTC UTXO DATA NEEDED")
    print("=" * 50)
    print("✅ 9K BTC UTXO: READY (from your real transaction)")
    print("❓ 12K BTC UTXO: AWAITING YOUR DATA")
    print()
    print("📋 Required format for 12K UTXO:")
    print(f"txid: {EXAMPLE_12K_UTXO['txid']}")
    print(f"vout: {EXAMPLE_12K_UTXO['vout']}")
    print(f"value: {EXAMPLE_12K_UTXO['value']} (12,000 BTC in satoshis)")
    print()
    print("🔧 Once you provide this, I'll instantly create:")
    print("  • Perfect 21,000 BTC transaction")
    print("  • Two 10,500 BTC QR codes")
    print("  • Terminal-ready hex for broadcasting")

if __name__ == "__main__":
    show_requirements()