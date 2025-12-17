import os
from cryptography.fernet import Fernet

DB_PATH = "db/database.db"
ENC_DB_PATH = "db/database_encrypted.db"
KEY_PATH = "db/secret.key"

with open(KEY_PATH, "rb") as f:
    key = f.read()

fernet = Fernet(key)

def encrypt_database():
    
    with open(DB_PATH, "rb") as f:
        data = f.read()

    encrypted_data = fernet.encrypt(data)

    with open(ENC_DB_PATH, "wb") as f:
        f.write(encrypted_data)

    # Optionally, remove the unencrypted file
    os.remove(DB_PATH)

    print("Database encrypted successfully!")
    print(f"Use '{KEY_PATH}' to decrypt it before editing or reading.")

def decrypt_database():

    # Decrypt the database
    with open(ENC_DB_PATH, "rb") as f:
        encrypted_data = f.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    with open(DB_PATH, "wb") as f:
        f.write(decrypted_data)

    print("Database decrypted successfully!")