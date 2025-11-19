from tkinter import *
import tkinter as tk
from core.database import retrieve_entry, delete_entry
from GUI.add_entry_window import add_entry_page
from functools import partial
from cryptography.fernet import Fernet
from core.encryption import decrypt_text



def vault_page(root,key):

    # Creates a fernet object using the key (can be used to encrypt/decrypt)
    fernet = Fernet(key)

    root.title("SafePass - Vault Page")
    root.geometry("1000x600")

    # Create grid columns and add weight
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)

    Label(root, text="Password Vault", font=("Arial", 18)).grid(row=0, column=0, columnspan=3, pady=10)

    # Displays "Website", "Username", "Password" in a row. Used as reference points.
    Label(root, text="Website", font=("Arial", 14)).grid(row=2, column=0, padx=10, pady=5)
    Label(root, text="Username", font=("Arial", 14)).grid(row=2, column=1, padx=10, pady=5)
    Label(root, text="Password", font=("Arial", 14)).grid(row=2, column=2, padx=10, pady=5)

    # Function that displays all the entries onto the vault page
    def load_entries():

        # Calls function to retrieve all the entries
        data = retrieve_entry()

        # Clears the old rows of entries
        for widget in root.grid_slaves():
            if int(widget.grid_info()["row"]) >= 3:
                widget.grid_forget()

        # Defines the starting row where the first set of entries will be displayed
        starting_row = 3

        for entry in data:

            # Retrieves each entry
            website = entry[1]
            username = entry[2]
            password = entry[3]

            # Decrypts website, username, password (encrypted in the table)
            decrypted_website = decrypt_text(website,fernet)
            decrypted_username = decrypt_text(username,fernet)
            decrypted_password = decrypt_text(password, fernet)

            Label(root, text=decrypted_website, font=("Arial", 12)).grid(row=starting_row, column=0, padx=10, pady=5) # Displays website
            Label(root, text=decrypted_username, font=("Arial", 12)).grid(row=starting_row, column=1, padx=10, pady=5) # Displays username
            Label(root, text=decrypted_password, font=("Arial", 12)).grid(row=starting_row, column=2, padx=10, pady=5) # Displays password

            # Calls function to delete entry and refreshes page
            def delete(entry_id):
                delete_entry(entry_id)
                load_entries()

            # Delete button which calls the delete function to delete the chosen entry
            delete_button = Button(root, text="Delete", font=("Arial", 12), command=partial(delete,entry[0]))
            delete_button.grid(row=starting_row, column=3, padx=10, pady=5)

            # Increment starting row
            starting_row = starting_row + 1

    # Function calls add_entry_page and then refreshes the page
    def add():

        # Temporarily disables button
        add_button.config(state=tk.DISABLED)

        win = add_entry_page(root, fernet) # Passes the fernet object to add entry page so encryption/decryption can be done
        root.wait_window(win) # Waits until the add entry window is closed
        load_entries() #  Once closed, page is refreshed

        add_button.config(state=tk.NORMAL)

    # Creates a "+" button 
    add_button = Button(root, text="+", font=("Arial", 18), pady=15, padx=15, command=add)
    add_button.grid(row=1, column=0, columnspan=3, pady=10)
    
    # Refreshes page
    load_entries()