import bcrypt
from core.database import get_connection

# Function to hash and store master password in database
def save_master_password(master_password):

    # Connects to database
    conn = get_connection()
    c = conn.cursor()

    # Hash the master password using random salt
    hashed_password = bcrypt.hashpw(master_password.encode(), bcrypt.gensalt())

    # Insert into database
    c.execute("INSERT INTO master_password (master_password) VALUES (?)", (hashed_password,))

    # Closes connection
    conn.commit()
    conn.close()

# Function to authenticate the user (check to see if entered master password is correct)
def authenticate_master_password(entered_password):

    # Connects to database
    conn = get_connection()
    c = conn.cursor()

    # Fetches stored master password and stores in a tuple
    c.execute("SELECT master_password FROM master_password")
    stored_hash = c.fetchone()
    
    # Extracts master password from tuple
    stored_hash = stored_hash[0]

    # Encodes the entered password (must be encoded into bytes before it is hashed)
    encoded_entered_password = entered_password.encode()

    # Compares entered password with stored hash
    # checkpw automatically salts and hashes the the entered 
    if bcrypt.checkpw(encoded_entered_password,stored_hash):
        return True                                 
