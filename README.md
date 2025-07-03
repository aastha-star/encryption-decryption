## 📌 Features

- 🔑 Automatic key generation and secure storage (`secret.key`)
- 📂 Encrypt and decrypt any file type
- ⚠️ Overwrites original files for security
- 🧩 Simple command-line interface
- 🚫 Robust error handling (missing files, invalid keys, etc.)

## 📦 Technologies Used

- Python 3.x
- [cryptography](https://cryptography.io/en/latest/) library (Fernet module)

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/file-encryption-tool.git
cd file-encryption-tool
````

### 2. Install Dependencies

```bash
pip install cryptography
```

### 3. Run the Tool

```bash
python encrypt_decrypt_tool.p

Follow the prompts to:

* Generate an encryption key
* Encrypt a file
* Decrypt a file

## 🛡️ Important Notes

* The tool uses **Fernet** encryption (AES-128-CBC + HMAC).
* Keep the `secret.key` file safe; without it, encrypted files cannot be recovered.
* The tool **overwrites original files**—backups are recommended.

## 👤 User Requirements

* Basic knowledge of using command-line and Python.
* Must have read/write access to target files.

## 🔧 Future Improvements

* GUI-based version for non-technical users
* Cloud storage integration
* Password-based key management
* Batch file encryption

## 📚 References

* [Python Cryptography Docs](https://cryptography.io/en/latest/)
* [Fernet Specification](https://cryptography.io/en/latest/fernet/)
* Python Official Documentation


**Contributors**:
Aastha Srivastava
**Supervisor**: Dr. Gunjan Mittal Roy
**Institution**: IILM University, Greater Noida
