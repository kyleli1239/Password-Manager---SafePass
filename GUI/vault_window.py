from tkinter import *
from tkinter import messagebox
from core.database import retrieve_entry, delete_entry
from GUI.add_entry_window import add_entry_page
from functools import partial

def vault_page(root):

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

            website = entry[1]
            username = entry[2]
            password = entry[3]

            Label(root, text=website, font=("Arial", 12)).grid(row=starting_row, column=0, padx=10, pady=5) # Displays website
            Label(root, text=username, font=("Arial", 12)).grid(row=starting_row, column=1, padx=10, pady=5) # Displays username
            Label(root, text=password, font=("Arial", 12)).grid(row=starting_row, column=2, padx=10, pady=5) # Displays password

            # Calls function to delete entry and refreshes page
            def delete(entry_id):
                delete_entry(entry_id)
                load_entries()

            # Delete button which calls the delete function to delete the chosen entry
            delete_button = Button(root, text="Delete", font=("Arial", 12), command=partial(delete,entry[0]))
            delete_button.grid(row=starting_row, column=3, padx=10, pady=5)

            # Increment starting row
            starting_row = starting_row + 1

    def add():
        add_entry_page(root)
        load_entries()

    # Creates a "+" button 
    Button(root, text="+", font=("Arial", 18), pady=15, padx=15, command=add).grid(row=1, column=0, columnspan=3, pady=10)
    
    load_entries()