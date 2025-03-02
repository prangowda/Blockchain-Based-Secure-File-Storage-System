from flask import Flask, request, jsonify, render_template
import hashlib
from web3 import Web3
from ipfs_upload import upload_to_ipfs

app = Flask(__name__)

# Connect to Blockchain (Ganache / Ethereum Node)
web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
contract_address = "YOUR_CONTRACT_ADDRESS"
abi = '[ YOUR_ABI_HERE ]'
contract = web3.eth.contract(address=contract_address, abi=abi)
owner_address = "YOUR_WALLET_ADDRESS"

# Generate Hash of File
def generate_file_hash(file_path):
    hasher = hashlib.sha256()
    with open(file_path, "rb") as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files["file"]
    file_path = "uploads/" + file.filename
    file.save(file_path)

    # Generate hash and store on IPFS
    file_hash = generate_file_hash(file_path)
    ipfs_hash = upload_to_ipfs(file_path)

    # Store on Blockchain
    tx = contract.functions.storeFile(file_hash, file.filename).transact({"from": owner_address})
    web3.eth.wait_for_transaction_receipt(tx)

    return jsonify({"file_hash": file_hash, "ipfs_hash": ipfs_hash})

@app.route("/verify", methods=["POST"])
def verify_file():
    file = request.files["file"]
    file_hash = generate_file_hash(file.filename)

    try:
        file_name, timestamp = contract.functions.verifyFile(file_hash).call()
        return jsonify({"status": "Valid", "file_name": file_name, "timestamp": timestamp})
    except:
        return jsonify({"status": "Invalid", "message": "File not found on blockchain"})

if __name__ == "__main__":
    app.run(debug=True)
