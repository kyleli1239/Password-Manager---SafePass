from tkinter import *
from GUI.signup_window import signup_page
from GUI.login_window import login_page
from core.database import initialise_database, get_connection
import os

# Paths to database file held in data
db_path = "data/SafePass_database.db"

# Checks to see if database exists. If not, initialises databbase
def start_app():
    if not os.path.exists(db_path):
        initialise_database()

    # Connects to database and using SQL, fetches 1st row in master_password table and stores/returns the result
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM master_password")
    result = c.fetchone()
    return result

# Runs main.py
if __name__ == "__main__":
    root = Tk()

    # If a result was returned in start_app, there is a master password 
    master_password_exists = start_app()
    if master_password_exists:
        login_page(root) # Login page displayed if master password exists
    else:
        signup_page(root) # Signup page displayed if master password is missing

    # Starts the GUI and loops
    root.mainloop()