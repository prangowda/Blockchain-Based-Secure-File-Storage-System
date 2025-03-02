# **Blockchain-Based File Verification System**  

### **📌 Description**  
This project is a **Blockchain-based file verification system** that securely stores file hashes on the **Ethereum blockchain**. It ensures **data integrity and authenticity**, allowing users to verify if a file has been altered.  

---

## **🚀 Features**
✅ **Store file hashes on the blockchain** for tamper-proof verification.  
✅ **Retrieve file details** to verify authenticity.  
✅ **Ethereum smart contract** for secure storage.  
✅ **Flask-based backend API** for easy integration.  
✅ **Web3.py for blockchain interaction**.  

---

## **🛠 Technologies Used**
- **Blockchain:** Ethereum (Ganache, Infura)  
- **Smart Contracts:** Solidity  
- **Backend:** Flask (Python)  
- **Blockchain Interaction:** Web3.py  
- **Frontend (Optional):** HTML, JavaScript (Web3.js)  

---

## **📂 Project Structure**
```
📦 Blockchain-File-Verification
 ┣ 📜 app.py                # Flask backend for API
 ┣ 📜 web3_connect.py       # Web3.py script for blockchain interaction
 ┣ 📜 smart_contract.sol    # Solidity smart contract
 ┣ 📜 requirements.txt      # Required Python libraries
 ┣ 📜 README.md             # Project documentation
 ┗ 📜 static/ & templates/  # (If a frontend is included)
```

---

## **🔧 Setup and Installation**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/prangowda/blockchain-file-verification.git
cd blockchain-file-verification
```

### **2️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3️⃣ Deploy the Smart Contract**
- Open **Remix IDE** or use **Truffle**.  
- Compile & deploy `smart_contract.sol` on **Ganache/Infura**.  
- Copy **contract address & ABI** to `web3_connect.py`.  

### **4️⃣ Run the Backend**
```bash
python app.py
```

### **5️⃣ Test API Endpoints**
Use **Postman** or **cURL**:
- **Store a file hash**:  
  ```bash
  curl -X POST http://127.0.0.1:5000/store -d "file_hash=123abc&file_name=document.pdf"
  ```
- **Verify a file hash**:  
  ```bash
  curl -X GET http://127.0.0.1:5000/verify?file_hash=123abc
  ```

---

## **🔗 API Endpoints**
| **Method** | **Endpoint**         | **Description**                            |
|------------|----------------------|--------------------------------------------|
| `POST`     | `/store`             | Store file hash and name on blockchain    |
| `GET`      | `/verify`            | Verify file integrity by hash             |

---

## **🔐 Security Considerations**
- Use **MetaMask** for secure wallet authentication.  
- Enable **HTTPS** for API communication.  
- Store **private keys securely** using `.env` files.  

---

## **🌟 Enhancements**
- ✅ Build a **React/Flutter UI** for a user-friendly interface.  
- ✅ Deploy the **smart contract on Ethereum testnet**.  
- ✅ Add **IPFS storage** for actual files (instead of only hashes).  
