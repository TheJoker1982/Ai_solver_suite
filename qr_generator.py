#!/usr/bin/env python3
"""
Industry-Grade Universal QR Code Generator
Bitcoin Transaction QR System with Perfect Compatibility
"""

import qrcode
from qrcode import constants
import base64
import json
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import os
import hashlib
import math

class IndustryQRGenerator:
    """Bitcoin industry-standard QR code generator with universal compatibility"""
    
    def __init__(self):
        self.qr_standards = {
            'bitcoin_uri': 'bitcoin:',
            'bip21': True,
            'error_correction': constants.ERROR_CORRECT_M,  # 15% error correction
            'box_size': 10,
            'border': 4,
            'version': None  # Auto-size
        }
    
    def create_bitcoin_qr(self, address, amount_btc=None, label=None, message=None):
        """Create Bitcoin URI QR code following BIP-21 standard"""
        
        # Build Bitcoin URI (BIP-21 compliant)
        bitcoin_uri = f"bitcoin:{address}"
        
        params = []
        if amount_btc is not None:
            # Convert to exact Bitcoin format (8 decimal places)
            amount_str = f"{amount_btc:.8f}".rstrip('0').rstrip('.')
            params.append(f"amount={amount_str}")
        
        if label:
            params.append(f"label={label}")
        
        if message:
            params.append(f"message={message}")
        
        if params:
            bitcoin_uri += "?" + "&".join(params)
        
        return self._generate_qr(bitcoin_uri, qr_type="bitcoin_payment")
    
    def create_transaction_qr(self, tx_hex):
        """Create QR for raw transaction hex"""
        return self._generate_qr(tx_hex, qr_type="raw_transaction")
    
    def create_address_qr(self, address):
        """Create simple address QR code"""
        return self._generate_qr(address, qr_type="bitcoin_address")
    
    def _generate_qr(self, data, qr_type="generic"):
        """Core QR generation with industry standards"""
        
        # Calculate optimal version for data
        data_length = len(data.encode('utf-8'))
        version = self._calculate_optimal_version(data_length)
        
        # Create QR instance with industry settings
        qr = qrcode.QRCode(
            version=version,
            error_correction=self.qr_standards['error_correction'],
            box_size=self.qr_standards['box_size'],
            border=self.qr_standards['border']
        )
        
        # Add data and optimize
        qr.add_data(data)
        qr.make(fit=True)
        
        # Generate high-quality image
        qr_image = qr.make_image(
            fill_color="black",
            back_color="white"
        )
        
        # Add metadata
        qr_data = {
            'image': qr_image,
            'data': data,
            'type': qr_type,
            'version': qr.version,
            'error_correction': 'M (15%)',
            'modules': qr.modules_count,
            'data_length': data_length,
            'uri': data if qr_type == "bitcoin_payment" else None
        }
        
        return qr_data
    
    def _calculate_optimal_version(self, data_length):
        """Calculate optimal QR version for data length"""
        # QR version capacity for ERROR_CORRECT_M (alphanumeric)
        capacities = [
            25, 47, 77, 114, 154, 195, 224, 279, 335, 395,  # 1-10
            468, 535, 619, 667, 758, 854, 938, 1046, 1153, 1249,  # 11-20
            1352, 1460, 1588, 1704, 1853, 1990, 2132, 2223, 2369, 2520,  # 21-30
            2677, 2840, 3009, 3183, 3351, 3537, 3729, 3927, 4087, 4296  # 31-40
        ]
        
        for version, capacity in enumerate(capacities, 1):
            if data_length <= capacity:
                return version
        
        return 40  # Maximum version
    
    def save_qr_image(self, qr_data, filename, add_label=False):
        """Save QR image with optional label"""
        
        img = qr_data['image']
        
        # Ensure output directory
        os.makedirs('output/qr_codes', exist_ok=True)
        filepath = f"output/qr_codes/{filename}"
        
        # Save high-quality PNG
        img.save(filepath, 'PNG')
        
        print(f"✅ QR saved: {filepath}")
        print(f"📊 Version: {qr_data['version']}, Modules: {qr_data['modules']}")
        print(f"🔗 Data: {qr_data['data'][:50]}{'...' if len(qr_data['data']) > 50 else ''}")
        
        return filepath
    
    def _add_label_to_qr(self, qr_img, qr_data):
        """Add descriptive label below QR code"""
        
        # Calculate new image size
        qr_width, qr_height = qr_img.size
        label_height = 60
        new_height = qr_height + label_height
        
        # Create new image with space for label
        new_img = Image.new('RGB', (qr_width, new_height), 'white')
        new_img.paste(qr_img, (0, 0, qr_width, qr_height))
        
        # Add text
        draw = ImageDraw.Draw(new_img)
        
        try:
            # Try to use a nice font
            font = ImageFont.truetype("/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf", 14)
        except:
            font = ImageFont.load_default()
        
        # Create label text based on type
        if qr_data['type'] == 'bitcoin_payment':
            label_text = f"Bitcoin Payment QR"
        elif qr_data['type'] == 'bitcoin_address':
            label_text = f"Bitcoin Address"
        else:
            label_text = f"Bitcoin {qr_data['type'].title()}"
        
        # Center text
        text_bbox = draw.textbbox((0, 0), label_text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        x_pos = (qr_width - text_width) // 2
        y_pos = qr_height + 20
        
        draw.text((x_pos, y_pos), label_text, fill='black', font=font)
        
        return new_img
    
    def create_payment_summary(self, address1, amount1, address2, amount2, tx_hex=None):
        """Create complete payment QR summary"""
        
        print("🎯 GENERATING INDUSTRY-GRADE QR CODES")
        print("=" * 60)
        
        # Generate QR codes
        qr1 = self.create_bitcoin_qr(address1, amount1, f"Payment 1: {amount1} BTC")
        qr2 = self.create_bitcoin_qr(address2, amount2, f"Payment 2: {amount2} BTC")
        
        # Save QR images
        file1 = self.save_qr_image(qr1, f"payment_1_{amount1:.0f}btc.png")
        file2 = self.save_qr_image(qr2, f"payment_2_{amount2:.0f}btc.png")
        
        # Transaction QR if provided
        tx_file = None
        if tx_hex:
            tx_qr = self.create_transaction_qr(tx_hex)
            tx_file = self.save_qr_image(tx_qr, "transaction_hex.png")
        
        # Summary
        summary = {
            'payment_1': {
                'address': address1,
                'amount_btc': amount1,
                'qr_file': file1,
                'uri': qr1['uri']
            },
            'payment_2': {
                'address': address2,
                'amount_btc': amount2,
                'qr_file': file2,
                'uri': qr2['uri']
            },
            'transaction': {
                'hex': tx_hex,
                'qr_file': tx_file
            } if tx_hex else None
        }
        
        return summary

def create_50_50_split_qrs(recipient_address, total_btc, tx_hex=None):
    """Create 50/50 split QR codes for Bitcoin payments"""
    
    qr_gen = IndustryQRGenerator()
    
    # Split amount
    split_amount = total_btc / 2
    
    print(f"\n🔄 CREATING 50/50 SPLIT QR CODES")
    print(f"💰 Total: {total_btc} BTC")
    print(f"📊 Each payment: {split_amount} BTC")
    print(f"📍 Address: {recipient_address}")
    
    # Create QRs for same address but different amounts/labels
    summary = qr_gen.create_payment_summary(
        recipient_address, split_amount,  # Payment 1
        recipient_address, split_amount,  # Payment 2  
        tx_hex
    )
    
    print(f"\n✅ QR CODES GENERATED")
    print(f"📁 Saved to: output/qr_codes/")
    print(f"🎯 Payment 1: {summary['payment_1']['qr_file']}")
    print(f"🎯 Payment 2: {summary['payment_2']['qr_file']}")
    
    return summary

# Test function
if __name__ == "__main__":
    # Test with your recipient address
    recipient = "1794B4ynTe3WA6VdCQWjg5EtPnYRuYZ45j" 
    total_amount = 21000  # From 12k + 9k UTXOs
    
    summary = create_50_50_split_qrs(recipient, total_amount)
    
    print(f"\n🔗 Bitcoin URIs Generated:")
    print(f"Payment 1: {summary['payment_1']['uri']}")
    print(f"Payment 2: {summary['payment_2']['uri']}")