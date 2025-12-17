import sqlite3

from ..encryption.encrypt import decrypt_database,encrypt_database

# Path to the database
DB_PATH = "db/database.db"

decrypt_database()

# Connect to the SQLite database
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

def find_all():
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