import sqlite3
import os
from cryptography.fernet import Fernet

from ..encryption.encrypt import encrypt_database

# Paths
DB_PATH = "db/database.db"
ENC_DB_PATH = "db/database_encrypted.db"
KEY_PATH = "db/secret.key"

def create_db():
    # Ensure the db directory exists
    if not os.path.exists('db'):
        os.makedirs('db')

    # --- Generate a key if it doesn't exist ---
    if not os.path.exists(KEY_PATH):
        key = Fernet.generate_key()
        with open(KEY_PATH, "wb") as f:
            f.write(key)
    else:
        with open(KEY_PATH, "rb") as f:
            key = f.read()


    # --- Create database ---
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    with open("app/backend/database/create/schema.sql", "r") as f:
        sql_script = f.read()
        cursor.executescript(sql_script)

    conn.commit()
    conn.close()

    print("Database created!")

    # --- Encrypt the database ---
    encrypt_database()
