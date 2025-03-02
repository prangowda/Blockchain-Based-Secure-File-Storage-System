from web3 import Web3

# Connect to Ethereum Network (Replace with your provider URL)
INFURA_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
GANACHE_URL = "http://127.0.0.1:7545"  # If using Ganache locally

# Connect Web3 to the blockchain network
web3 = Web3(Web3.HTTPProvider(GANACHE_URL))  # Change to INFURA_URL if on mainnet/testnet

# Check if connected
if web3.is_connected():
    print("✅ Connected to Ethereum Blockchain")
else:
    print("❌ Connection Failed")

# Smart Contract Address and ABI (Replace with your deployed contract details)
contract_address = "YOUR_SMART_CONTRACT_ADDRESS"
contract_abi = '[ YOUR_ABI_HERE ]'

# Load Smart Contract
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# Wallet Address (Replace with your wallet that deployed the contract)
owner_address = "YOUR_WALLET_ADDRESS"

def store_file_on_blockchain(file_hash, file_name):
    """Stores the file hash and name on the blockchain"""
    txn = contract.functions.storeFile(file_hash, file_name).transact({"from": owner_address})
    receipt = web3.eth.wait_for_transaction_receipt(txn)
    return receipt

def verify_file_on_blockchain(file_hash):
    """Verifies file integrity on the blockchain"""
    try:
        file_name, timestamp = contract.functions.verifyFile(file_hash).call()
        return {"file_name": file_name, "timestamp": timestamp, "status": "Valid"}
    except:
        return {"status": "Invalid", "message": "File not found on blockchain"}
