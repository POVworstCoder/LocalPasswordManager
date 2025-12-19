import sqlite3

from ..encryption.encrypt import decrypt_database,encrypt_database
DB_PATH = "db/database.db"

def create_account(username="",email="",site_url="",password=""):
    decrypt_database()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(f"""
            INSERT INTO account (username,email,site_url,password) VALUES 
                ('{username}','{email}','{site_url}','{password}')
        """)
    
    conn.commit()
    conn.close()

    encrypt_database()

    print("Succesfully added new account")
    return True

def edit_account_id_column(id:int, column:str, data:str):
    if not id or not column:
        print("Account, object not found! or column missing")
        return False

    decrypt_database()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(f"""
            UPDATE account SET {column}='{data}' WHERE id = '{id}'
        """)    

    conn.commit()
    conn.close()

    encrypt_database()

    print(f"Successfully updated column: {column}")