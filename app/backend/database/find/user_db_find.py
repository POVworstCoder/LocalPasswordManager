import sqlite3

from ..encryption.encrypt import decrypt_database,encrypt_database

# Path to the database
DB_PATH = "db/database.db"


def find_all():
    decrypt_database()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    # Execute SELECT * query
    cursor.execute("SELECT * FROM account")

    # Fetch all results
    rows = cursor.fetchall()

    # Loop through the rows and print them
    for row in rows:
        print(row)

    encrypt_database()
    # Close the connection
    conn.close()
    
    return rows

def find_by_id(id: int):
    decrypt_database()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(f"""
        SELECT * FROM account
        WHERE id =  {id}
    """)

    row = cursor.fetchall()

    print(row)

    encrypt_database()

    conn.close()

    return row