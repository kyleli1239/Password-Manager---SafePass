import bcrypt
from core.database import get_connection
import os
from core.encryption import derive_key

# Function to hash and store master password in database
def save_master_password(master_password):

    # Connects to database
    conn = get_connection()
    c = conn.cursor()

    # Hash the master password using random salt
    hashed_password = bcrypt.hashpw(master_password.encode(), bcrypt.gensalt())

    # Generates random 16 byte salt
    generated_salt = os.urandom(16)

    # Insert into database
    c.execute("INSERT INTO master_password (master_password, salt) VALUES (?,?)", (hashed_password,generated_salt))

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

        # Retrieves the salt stored in the master_password table
        c.execute("SELECT salt FROM master_password")
        stored_salt = c.fetchone()
        stored_salt = stored_salt[0]

        # Returns the derived key
        key = derive_key(entered_password, stored_salt)
        return key 