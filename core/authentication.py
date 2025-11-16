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