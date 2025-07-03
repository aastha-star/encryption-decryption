from cryptography.fernet import InvalidToken, Fernet
import os

KEY_FILE = "Secret.key"

def generate_key():
    """Generates and saves a new encryption key"""
    try:
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)
        print(f"✅ New encryption key generated at {os.path.abspath(KEY_FILE)}")
    except Exception as e:
        print(f"🔴 Failed to generate key: {str(e)}")
        exit(1)

def load_key():
    """Loads the encryption key from file"""
    try:
        if not os.path.exists(KEY_FILE):
            raise FileNotFoundError(f"Key file '{os.path.abspath(KEY_FILE)}' not found")
        return open(KEY_FILE, "rb").read()
    except Exception as e:
        print(f"🔴 Key loading failed: {str(e)}")
        exit(1)

def file_operation(action, filename, key):
    """Handles encryption/decryption operations"""
    try:
        full_path = os.path.abspath(filename)
        print(f"🕵️  Checking: {full_path}")
        
        if not os.path.exists(full_path):
            raise FileNotFoundError(f"File not found at {full_path}")
            
        if action == 'encrypt':
            fernet = Fernet(key)
            with open(filename, "rb") as file:
                file_data = file.read()
            encrypted_data = fernet.encrypt(file_data)
            with open(filename, "wb") as file:
                file.write(encrypted_data)
            return True
            
        elif action == 'decrypt':
            fernet = Fernet(key)
            with open(filename, "rb") as file:
                encrypted_data = file.read()
            decrypted_data = fernet.decrypt(encrypted_data)
            with open(filename, "wb") as file:
                file.write(decrypted_data)
            return True
            
    except InvalidToken:
        print("🔴 Invalid key or corrupted data!")
    except Exception as e:
        print(f"🔴 Operation failed: {str(e)}")
    return False

# Main program flow
print(f"📁 Current working directory: {os.getcwd()}")
choice = input("Enter 'E' to encrypt or 'D' to decrypt a file: ").lower()

if choice == 'e':
    filename = input("Enter file name to encrypt (with extension): ").strip()
    if not os.path.exists(filename):
        print(f"🔴 File not found at: {os.path.abspath(filename)}")
        exit(1)
    
    if not os.path.exists(KEY_FILE):
        generate_key()
    
    key = load_key()
    if file_operation('encrypt', filename, key):
        print("✅ Encryption successful!")
        print(f"🔑 Key location: {os.path.abspath(KEY_FILE)}")

elif choice == 'd':
    filename = input("Enter file name to decrypt (with extension): ").strip()
    key = load_key()  # Will exit if key not found
    if file_operation('decrypt', filename, key):
        print("✅ Decryption successful!")

else:
    print("⚠️ Invalid choice. Please enter 'E' or 'D'.")
