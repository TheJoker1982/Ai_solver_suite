
from bitcoinlib.transactions import Transaction
from bitcoinlib.services.services import Service
from decimal import Decimal
from typing import List, Dict, Tuple, Union
import logging
import sys
import os
import time
import socket
from datetime import datetime

# Constants
SATOSHI = 100000000
DUST_THRESHOLD = 546
MIN_FEE_RATE = 1  # sat/byte
MAX_FEE_RATE = 500  # sat/byte
SEND_AMOUNT = 3000000000000  # 30000 BTC
FEE = 500000000  # 5 BTC
RECIPIENT_ADDRESS = '187tbMahXLjkRFJ6DNVeGwdS1nvF6GvDEZ'
CHANGE_ADDRESS = '12ib7dApVFvg82TXKycWBNpN8kFyiAN1dr'
MAX_TRANSACTION_SIZE = 100000  # bytes
MAX_INPUTS = 1000
MIN_CONFIRMATIONS = 1
MAX_RETRIES = 3
RETRY_DELAY = 2  # seconds
TIMEOUT = 30  # seconds
MAX_BTC = 21_000_000
LOG_FILE = f"bitcoin_transaction_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

HOST = '0.0.0.0'  # Standard loopback interface address (localhost)
PORT = 8000        # Port to listen on (non-privileged ports are > 1023)

# Setup logging with both file and console handlers
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(LOG_FILE)
    ]
)
logger = logging.getLogger(__name__)

# Exception classes
class TransactionError(Exception):
    """Base exception for transaction-related errors"""
    pass

class InsufficientFundsError(TransactionError):
    """Raised when there are insufficient funds"""
    pass

class InvalidAddressError(TransactionError):
    """Raised when an invalid address is provided"""
    pass

class UTXOError(TransactionError):
    """Raised when there are UTXO-related issues"""
    pass

class ValidationError(TransactionError):
    """Raised when validation fails"""
    pass

class NetworkError(TransactionError):
    """Raised when network-related issues occur"""
    pass

def retry_on_failure(max_retries: int = MAX_RETRIES, delay: int = RETRY_DELAY):
    """
    Decorator for retrying functions on failure
    Args:
        max_retries: Maximum number of retry attempts
        delay: Delay between retries in seconds
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_retries - 1:
                        raise
                    logger.warning(f"Attempt {attempt + 1} failed: {str(e)}. Retrying...")
                    time.sleep(delay)
            return None
        return wrapper
    return decorator

def estimate_transaction_size(input_count: int, output_count: int) -> int:
    """
    Estimate transaction size in bytes
    Args:
        input_count: Number of inputs
        output_count: Number of outputs
    Returns:
        int: Estimated transaction size in bytes
    """
    return (input_count * 148) + (output_count * 34) + 10  # Added safety margin

@retry_on_failure()
def create_transaction(valid_utxos: List[Dict], total_needed: int) -> Tuple[Transaction, int]:
    """
    Create and prepare the transaction
    Args:
        valid_utxos: List of validated UTXOs
        total_needed: Total amount needed for transaction
    Returns:
        Tuple containing Transaction object and amount added
    Raises:
        TransactionError: If transaction creation fails
    """
    tx = Transaction()
    amount_added = 0
    inputs_added = 0

    for utxo in valid_utxos:
        if inputs_added >= MAX_INPUTS:
            raise TransactionError(f"Maximum inputs limit ({MAX_INPUTS}) exceeded")

        tx.add_input(utxo['txid'], utxo['vout'])
        amount_added += int(utxo['value'])
        inputs_added += 1

        # Estimate current transaction size
        est_size = estimate_transaction_size(inputs_added, 2)
        if est_size > MAX_TRANSACTION_SIZE:
            raise TransactionError("Estimated transaction size exceeds maximum limit")

    return tx, amount_added

def find_utxos():
    """Find real UTXOs from blockchain using live data"""
    import requests
    
    # Get private key from environment
    private_key = os.getenv('PRIVATE_KEY')
    if not private_key:
        logger.error("No private key found in environment")
        return []
    
    try:
        from bitcoinlib.keys import Key
        key = Key(private_key)
        address = key.address()
        
        # Query real blockchain for UTXOs
        api_urls = [
            f"https://blockstream.info/api/address/{address}/utxo",
            f"https://api.blockcypher.com/v1/btc/main/addrs/{address}?unspentOnly=true"
        ]
        
        for api_url in api_urls:
            try:
                response = requests.get(api_url, timeout=30)
                if response.status_code == 200:
                    data = response.json()
                    
                    if 'blockstream.info' in api_url:
                        return [
                            {
                                'txid': utxo['txid'],
                                'vout': utxo['vout'],
                                'value': utxo['value']
                            }
                            for utxo in data
                        ]
                    elif 'blockcypher.com' in api_url:
                        return [
                            {
                                'txid': utxo['tx_hash'],
                                'vout': utxo['tx_output_n'],
                                'value': utxo['value']
                            }
                            for utxo in data.get('txrefs', [])
                        ]
                        
            except Exception as e:
                logger.warning(f"API {api_url} failed: {e}")
                continue
        
        logger.error("All UTXO APIs failed")
        return []
        
    except Exception as e:
        logger.error(f"Error finding real UTXOs: {e}")
        return []

@retry_on_failure()
def broadcast_transaction(raw_hex: str) -> str:
    """
    Broadcast a signed transaction to the Bitcoin network
    Args:
        raw_hex: Raw transaction hex string
    Returns:
        str: Transaction ID if successful, None if failed
    Raises:
        NetworkError: If broadcasting fails
    """
    try:
        service = Service()
        result = service.sendrawtransaction(raw_hex)
        logger.info(f"Transaction broadcast successful: {result}")
        return result
    except Exception as e:
        logger.error(f"Transaction broadcast failed: {str(e)}")
        raise NetworkError(f"Failed to broadcast transaction: {str(e)}")

def send_bitcoin():
    # First find available UTXOs
    utxos = find_utxos()
    if not utxos:
        print("No available UTXOs found")
        return

    # Calculate total available balance
    total_available = sum(int(utxo['value']) for utxo in utxos)
    print(f"\nTotal available balance: {total_available / 100000000:.8f} BTC")

    # Set fixed amounts - 30000 BTC with 5 BTC fee
    send_amount = int(3000000000000)  # Exactly 30000 BTC
    fee = int(500000000)  # 5 BTC fee

    total_needed = send_amount + fee
    if total_available < total_needed:
        print("\nERROR: INSUFFICIENT FUNDS")
        print(f"Required: {total_needed / 100000000:.8f} BTC")
        print(f"Available: {total_available / 100000000:.8f} BTC")
        return

    print("\n=== VERIFYING LARGE TRANSACTION ===")
    print(f"Sending: {send_amount / 100000000:.8f} BTC")
    print(f"Fee: {fee / 100000000:.8f} BTC")
    confirmation = input("Type 'CONFIRM' to proceed: ")
    if confirmation != "CONFIRM":
        print("Transaction cancelled")
        return

    recipient_address = RECIPIENT_ADDRESS

    # Create transaction 
    tx = Transaction()

    # Add inputs from found UTXOs
    amount_added = 0
    for utxo in utxos:
        if 'txid' not in utxo or 'vout' not in utxo:
            continue

        tx.add_input(utxo['txid'], utxo['vout'])
        amount_added += utxo['value']
        if amount_added >= total_needed:
            break

    # Add output for main recipient
    tx.add_output(send_amount, recipient_address)

    # Calculate and add change output
    change_amount = amount_added - send_amount - fee
    if change_amount > 0:
        tx.add_output(change_amount, CHANGE_ADDRESS)

    raw_hex = ""  # Initialize raw_hex to avoid unbound local variable error

    try:
        private_key = os.getenv('PRIVATE_KEY')
        if not private_key:
            raise ValueError("Error: PRIVATE_KEY not found in environment variables")

        signed = tx.sign(private_key)
        raw_hex = tx.raw()
        print("\n=========== TRANSACTION INFO ===========")
        print(f"Amount: {send_amount / 100000000:.8f} BTC")
        print(f"Fee: {fee / 100000000:.8f} BTC")
        print(f"Total needed: {total_needed / 100000000:.8f} BTC")
        print(f"Available balance: {total_available / 100000000:.8f} BTC")

        # Broadcast the transaction
        broadcast_result = broadcast_transaction(raw_hex)
        if broadcast_result:
            print(f"\nTransaction broadcast successful!")
            print(f"Transaction ID: {broadcast_result}")
        else:
            print("\nTransaction broadcast failed!")

    except Exception as e:
        print(f"Error during transaction signing: {e}")

def start_socket_server():
    """Start a simple socket server"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server listening on {HOST}:{PORT}")
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)

def analyze_real_transaction():
    """Analyze real Bitcoin transactions from blockchain"""
    import requests
    
    private_key = os.getenv('PRIVATE_KEY')
    if not private_key:
        print("❌ No private key found. Cannot analyze real transactions.")
        return
    
    try:
        from bitcoinlib.keys import Key
        key = Key(private_key)
        address = key.address()
        
        print(f"\n=== REAL TRANSACTION ANALYSIS ===")
        print(f"Address: {address}")
        
        # Get real transaction history
        api_url = f"https://blockstream.info/api/address/{address}/txs"
        response = requests.get(api_url, timeout=30)
        
        if response.status_code == 200:
            transactions = response.json()
            
            if transactions:
                print(f"\nFound {len(transactions)} real transactions:")
                
                for i, tx in enumerate(transactions[:5]):  # Show first 5
                    print(f"\nTransaction #{i+1}:")
                    print(f"TXID: {tx['txid']}")
                    print(f"Block Height: {tx.get('status', {}).get('block_height', 'Unconfirmed')}")
                    print(f"Fee: {tx.get('fee', 0)} satoshis")
                    
                    # Analyze inputs
                    total_input = 0
                    for inp in tx.get('vin', []):
                        if 'prevout' in inp:
                            total_input += inp['prevout'].get('value', 0)
                    
                    # Analyze outputs
                    total_output = 0
                    for out in tx.get('vout', []):
                        total_output += out.get('value', 0)
                    
                    print(f"Total Input: {total_input / 100000000:.8f} BTC")
                    print(f"Total Output: {total_output / 100000000:.8f} BTC")
                    print(f"Actual Fee: {(total_input - total_output) / 100000000:.8f} BTC")
            else:
                print("No transactions found for this address")
        else:
            print(f"❌ Failed to fetch transactions: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Error analyzing real transactions: {e}")

if __name__ == "__main__":
    print("🔍 REAL BITCOIN TRANSACTION ANALYZER")
    print("=====================================")
    print("⚠️  NO MOCK DATA - REAL BLOCKCHAIN ONLY")
    
    analyze_real_transaction()
    
    print("\n🔗 Real UTXO Analysis:")
    utxos = find_utxos()
    if utxos:
        total_value = sum(utxo['value'] for utxo in utxos)
        print(f"Found {len(utxos)} real UTXOs")
        print(f"Total value: {total_value / 100000000:.8f} BTC")
        
        for i, utxo in enumerate(utxos[:3]):  # Show first 3
            print(f"UTXO {i+1}: {utxo['value'] / 100000000:.8f} BTC")
    else:
        print("No UTXOs found")
    
    print("======================================")
