import requests

IPFS_API = "http://127.0.0.1:5001/api/v0/add"

def upload_to_ipfs(file_path):
    with open(file_path, "rb") as file:
        response = requests.post(IPFS_API, files={"file": file})
        ipfs_hash = response.json()["Hash"]
        return ipfs_hash
