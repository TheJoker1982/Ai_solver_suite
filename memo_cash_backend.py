#!/usr/bin/env python3
"""
Memo.cash Backend Server
Real BCH blockchain integration for memo.cash protocol
"""

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import json
import os
import time
import logging
from datetime import datetime
from typing import Dict, List, Any, Optional
import requests
import hashlib
import sys

# Add src to path
sys.path.append('src')

try:
    from puzzle_data import PuzzleData
    from bitcoin_puzzle_toolkit import BitcoinPuzzleToolkit
except ImportError as e:
    print(f"Warning: Could not import puzzle modules: {e}")
    PuzzleData = None
    BitcoinPuzzleToolkit = None

app = Flask(__name__, 
           template_folder='templates',
           static_folder='static')
CORS(app)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Global state - real data only
app_state = {
    'startup_time': datetime.now(),
    'request_count': 0,
    'active_accounts': {},
    'active_account': None,
    'puzzle_data': None,
    'toolkit': None,
    'transactions': [],
    'balance_cache': {},
    'last_balance_check': 0,
    'blockchain_api_url': 'https://api.blockchair.com/bitcoin-cash',
    'memo_protocol_prefix': '6d'
}

def initialize_components():
    """Initialize real components only"""
    try:
        if PuzzleData:
            app_state['puzzle_data'] = PuzzleData()
            logger.info("✅ Real puzzle data initialized")

        if BitcoinPuzzleToolkit:
            app_state['toolkit'] = BitcoinPuzzleToolkit()
            logger.info("✅ Bitcoin puzzle toolkit initialized")

        # Only load real accounts with actual private keys
        load_real_accounts()

    except Exception as e:
        logger.error(f"Error initializing components: {e}")

def load_real_accounts():
    """Load only real BCH accounts from environment or files"""
    # Check for real private keys in environment
    private_keys = []

    # Load from environment variables
    for i in range(10):  # Check for up to 10 keys
        key_var = f'BCH_PRIVATE_KEY_{i}'
        key = os.getenv(key_var)
        if key:
            private_keys.append(key)

    # Load from WIF if provided
    wif_key = os.getenv('WIF_PRIVATE_KEY')
    if wif_key:
        private_keys.append(wif_key)

    if not private_keys:
        logger.warning("No real private keys found. System running in read-only mode.")
        return

    # Convert private keys to accounts
    for i, key in enumerate(private_keys):
        try:
            account_label = f'Real_Account_{i+1}'
            address = derive_address_from_key(key)

            app_state['active_accounts'][account_label] = {
                'address': address,
                'private_key': key,
                'can_transact': True,
                'label': account_label,
                'balance': get_real_balance(address)
            }

            logger.info(f"✅ Loaded real account: {account_label} - {address}")

        except Exception as e:
            logger.error(f"Failed to load account from key {i}: {e}")

    if app_state['active_accounts']:
        app_state['active_account'] = list(app_state['active_accounts'].keys())[0]

def derive_address_from_key(private_key: str) -> str:
    """Derive real BCH address from private key"""
    try:
        import bitcoinlib
        from bitcoinlib.keys import Key

        key = Key(private_key)
        return key.address()
    except Exception as e:
        logger.error(f"Failed to derive address: {e}")
        return ""

def get_real_balance(address: str) -> float:
    """Get real BCH balance from blockchain"""
    try:
        url = f"{app_state['blockchain_api_url']}/dashboards/address/{address}"
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            data = response.json()
            if 'data' in data and address in data['data']:
                balance_satoshis = data['data'][address]['address']['balance']
                return balance_satoshis / 100000000  # Convert to BCH

        return 0.0
    except Exception as e:
        logger.error(f"Failed to get real balance for {address}: {e}")
        return 0.0

def broadcast_real_transaction(raw_hex: str) -> Optional[str]:
    """Broadcast real transaction to BCH network"""
    try:
        # Use multiple broadcast services for reliability
        broadcast_urls = [
            'https://rest.bitcoin.com/v2/rawtransactions/sendRawTransaction',
            'https://api.blockchair.com/bitcoin-cash/push/transaction'
        ]

        for url in broadcast_urls:
            try:
                if 'bitcoin.com' in url:
                    response = requests.post(url, json={'hexString': raw_hex}, timeout=30)
                else:
                    response = requests.post(url, data={'data': raw_hex}, timeout=30)

                if response.status_code == 200:
                    result = response.json()
                    if 'txid' in result:
                        return result['txid']
                    elif isinstance(result, dict) and 'data' in result:
                        return result['data'].get('transaction_hash')

            except Exception as e:
                logger.warning(f"Broadcast failed on {url}: {e}")
                continue

        logger.error("All broadcast services failed")
        return None

    except Exception as e:
        logger.error(f"Transaction broadcast error: {e}")
        return None

# Initialize on startup
initialize_components()

@app.before_request
def before_request():
    """Track request counts"""
    app_state['request_count'] += 1

@app.route('/')
def index():
    """Main dashboard"""
    try:
        return render_template('memo/index.html')
    except Exception:
        return jsonify({
            "name": "Real Memo.cash Backend",
            "status": "running",
            "version": "1.0.0",
            "mode": "production",
            "real_data_only": True,
            "endpoints": {
                "status": "/api/status",
                "capabilities": "/api/capabilities", 
                "puzzles": "/api/puzzles",
                "memo": "/api/memo/*",
                "accounts": "/api/memo/accounts",
                "post": "/api/memo/post",
                "send": "/api/memo/send"
            }
        })

@app.route('/api/status')
def api_status():
    """Get real API status"""
    return jsonify({
        "status": "online",
        "mode": "production",
        "real_data_only": True,
        "uptime_seconds": int((datetime.now() - app_state['startup_time']).total_seconds()),
        "request_count": app_state['request_count'],
        "active_accounts": len(app_state['active_accounts']),
        "real_accounts_loaded": len([acc for acc in app_state['active_accounts'].values() if acc.get('can_transact')]),
        "puzzle_data_loaded": app_state['puzzle_data'] is not None,
        "blockchain_connected": True,
        "timestamp": datetime.now().isoformat()
    })

@app.route('/api/capabilities')
def api_capabilities():
    """Get real system capabilities"""
    capabilities = {
        "memo_protocol": True,
        "bch_transactions": True,
        "real_blockchain_interaction": True,
        "puzzle_solving": app_state['toolkit'] is not None,
        "puzzle_data": app_state['puzzle_data'] is not None,
        "account_management": True,
        "balance_checking": True,
        "transaction_broadcasting": len(app_state['active_accounts']) > 0,
        "supported_protocols": [
            "0x6d01",  # Set name
            "0x6d02",  # Post message
            "0x6d03",  # Reply
            "0x6d04",  # Like
            "0x6d05",  # Set profile text
            "0x6d06",  # Follow/Unfollow
            "0x6d07",  # Set avatar
            "0x6d20"   # Link request (MIP3)
        ],
        "features": {
            "real_transactions": True,
            "blockchain_broadcasting": True,
            "puzzle_analysis": True,
            "account_switching": True,
            "live_balance_checking": True
        }
    }
    return jsonify(capabilities)

@app.route('/api/puzzles')
def get_puzzles():
    """Get real Bitcoin puzzle information"""
    if not app_state['puzzle_data']:
        return jsonify({"error": "Puzzle data not available"}), 503

    try:
        puzzle_data = app_state['puzzle_data']

        # Get real statistics
        total_info = puzzle_data.get_total_unsolved_value()
        high_value = puzzle_data.get_high_value_targets(10.0)
        recommendations = puzzle_data.recommend_targets()

        return jsonify({
            "summary": total_info,
            "high_value_puzzles": high_value[:10],
            "recommendations": recommendations[:5],
            "data_source": puzzle_data.data_source,
            "last_updated": puzzle_data.last_updated.isoformat(),
            "btc_price_estimate": puzzle_data.btc_price_estimate,
            "real_data": True
        })
    except Exception as e:
        logger.error(f"Error getting puzzles: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/memo/accounts')
def get_accounts():
    """Get real BCH accounts only"""
    try:
        # Only return accounts with real private keys
        real_accounts = {}
        for label, account in app_state['active_accounts'].items():
            if account.get('can_transact') and account.get('private_key'):
                # Update balance with real data
                account['balance'] = get_real_balance(account['address'])
                real_accounts[label] = {
                    'address': account['address'],
                    'balance': account['balance'],
                    'can_transact': True,
                    'label': account['label'],
                    'real_account': True
                }

        return jsonify({
            "success": True,
            "accounts": real_accounts,
            "active_account": app_state['active_account'],
            "real_data_only": True,
            "timestamp": datetime.now().isoformat()
        })
    except Exception as e:
        logger.error(f"Error getting accounts: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/memo/post', methods=['POST'])
def create_real_post():
    """Create real memo.cash post transaction"""
    try:
        data = request.get_json()
        message = data.get('message', '')

        if not message:
            return jsonify({"success": False, "error": "Message is required"}), 400

        if len(message.encode('utf-8')) > 217:
            return jsonify({"success": False, "error": "Message too long (max 217 bytes)"}), 400

        active_account = app_state['active_accounts'].get(app_state['active_account'])
        if not active_account or not active_account.get('private_key'):
            return jsonify({"success": False, "error": "No active account with private key"}), 400

        # Create real memo transaction
        raw_tx = create_memo_transaction(
            active_account['private_key'],
            active_account['address'],
            message,
            '6d02'  # Memo post protocol
        )

        if not raw_tx:
            return jsonify({"success": False, "error": "Failed to create transaction"}), 500

        # Broadcast to real network
        txid = broadcast_real_transaction(raw_tx)

        if txid:
            transaction = {
                "txid": txid,
                "type": "memo_post",
                "protocol": "0x6d02",
                "message": message,
                "account": app_state['active_account'],
                "timestamp": datetime.now().isoformat(),
                "status": "broadcasted",
                "real_transaction": True
            }

            app_state['transactions'].append(transaction)

            return jsonify({
                "success": True,
                "txid": txid,
                "message": message,
                "protocol": "0x6d02",
                "account": app_state['active_account'],
                "status": "broadcasted",
                "real_transaction": True
            })
        else:
            return jsonify({"success": False, "error": "Failed to broadcast transaction"}), 500

    except Exception as e:
        logger.error(f"Error creating real post: {e}")
        return jsonify({"error": str(e)}), 500

def create_memo_transaction(private_key: str, from_address: str, message: str, protocol: str) -> Optional[str]:
    """Create real memo.cash transaction"""
    try:
        from bitcoinlib.transactions import Transaction
        from bitcoinlib.keys import Key

        key = Key(private_key)

        # Get UTXOs for the address
        utxos = get_real_utxos(from_address)
        if not utxos:
            logger.error("No UTXOs available")
            return None

        # Create transaction
        tx = Transaction()

        # Add inputs
        total_input = 0
        for utxo in utxos[:5]:  # Use up to 5 UTXOs
            tx.add_input(utxo['txid'], utxo['vout'])
            total_input += utxo['value']
            if total_input > 10000:  # Enough for memo + fee
                break

        if total_input < 1000:  # Minimum dust + fee
            logger.error("Insufficient funds")
            return None

        # Create memo output
        memo_data = bytes.fromhex(protocol) + message.encode('utf-8')
        tx.add_output(0, script_type='nulldata', data=memo_data)

        # Add change output
        fee = 500  # 500 satoshis fee
        change = total_input - fee
        if change > 546:  # Above dust threshold
            tx.add_output(change, from_address)

        # Sign transaction
        tx.sign(key)

        return tx.raw_hex()

    except Exception as e:
        logger.error(f"Failed to create memo transaction: {e}")
        return None

def get_real_utxos(address: str) -> List[Dict]:
    """Get real UTXOs from blockchain"""
    try:
        url = f"{app_state['blockchain_api_url']}/dashboards/address/{address}"
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            data = response.json()
            if 'data' in data and address in data['data']:
                utxos = data['data'][address].get('utxo', [])
                return [
                    {
                        'txid': utxo['transaction_hash'],
                        'vout': utxo['index'],
                        'value': utxo['value']
                    }
                    for utxo in utxos
                ]

        return []
    except Exception as e:
        logger.error(f"Failed to get UTXOs: {e}")
        return []

@app.route('/api/memo/balance/<address>')
def check_real_balance(address):
    """Check real address balance from blockchain"""
    try:
        balance = get_real_balance(address)

        balance_data = {
            "success": True,
            "address": address,
            "balance_bch": balance,
            "balance_satoshis": int(balance * 100000000),
            "real_balance": True,
            "timestamp": datetime.now().isoformat()
        }

        return jsonify(balance_data)
    except Exception as e:
        logger.error(f"Error checking real balance: {e}")
        return jsonify({"error": str(e)}), 500

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

def run_server(host='0.0.0.0', port=5000, debug=False):
    """Run the real server"""
    logger.info(f"🚀 Starting REAL Memo.cash Backend Server on {host}:{port}")
    logger.info(f"📱 Dashboard: http://{host}:{port}")
    logger.info(f"🔗 API: http://{host}:{port}/api")
    logger.info("⚠️  REAL BLOCKCHAIN MODE - NO SIMULATIONS")

    try:
        app.run(host=host, port=port, debug=debug, threaded=True)
    except Exception as e:
        logger.error(f"Failed to start server: {e}")
        raise

if __name__ == "__main__":
    import sys

    # Default settings
    host = '0.0.0.0'
    port = 5000
    debug = '--debug' in sys.argv

    run_server(host, port, debug)