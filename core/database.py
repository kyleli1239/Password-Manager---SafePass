import sqlite3

# Paths to database file held in data
db_path = "data/SafePass_database.db"

# If file exists in db_path, creates connection to that file
def get_connection():
    return sqlite3.connect(db_path)

# If file doesn't exist in db_path, create a new database
def initialise_database():

    # Create database
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    # Table for master_password
    c.execute(""" 
    CREATE TABLE IF NOT EXISTS master_password(
    master_id INTEGER PRIMARY KEY,
    master_password TEXT,
    salt BLOB);
    """)

    # Table for password_vault
    c.execute("""
    CREATE TABLE IF NOT EXISTS password_vault(
    entry_id INTEGER PRIMARY KEY,
    master_id INTEGER,
    website TEXT,
    username TEXT,
    password TEXT,
    FOREIGN KEY (master_id) REFERENCES master_password(master_id));
    """)

# Function to store entries in the database
def add_entry(master_id, website, username, password):
    
    # Connects to database
    conn = get_connection()
    c = conn.cursor()

    # Inserts the parameters into the password_vault table in the database
    c.execute("""INSERT INTO password_vault (master_id, website, username, password) 
              VALUES (?, ?, ?, ?)""",
              (master_id, website, username, password))
    
    # Commits changes to database and closes connection
    conn.commit()
    conn.close()
    
# Function to retrieve all the entries in the database
def retrieve_entry():

    # Connects to database
    conn = get_connection()
    c = conn.cursor()

    # Fetches and returns the entries and entry_id from database
    c.execute("SELECT entry_id, website, username, password FROM password_vault")
    rows = c.fetchall()
    return rows

# Function to delete specific entries
def delete_entry(entry_id):

    # Connections to database
    conn = get_connection()
    c = conn.cursor()

    # Deletes row of specific entry id
    c.execute("DELETE FROM password_vault WHERE entry_id = ?", (entry_id,))
    
    # Commits changes to database and closes connection
    conn.commit()
    conn.close()