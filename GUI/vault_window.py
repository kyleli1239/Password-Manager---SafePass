from tkinter import *
from tkinter import messagebox

def vault_page(root):

    root.title("SafePass - Vault Page")
    root.geometry("1000x600")

    # Create grid columns and add weight
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)

    Label(root, text="Password Vault", font=("Arial", 18)).grid(row=0, column=0, columnspan=3, pady=10)

    # Displays "W"ebsite", "Username", "Password" in a row. Used as reference points.
    Label(root, text="Website", font=("Arial", 14)).grid(row=2, column=0, padx=10, pady=5)
    Label(root, text="Username", font=("Arial", 14)).grid(row=2, column=1, padx=10, pady=5)
    Label(root, text="Password", font=("Arial", 14)).grid(row=2, column=2, padx=10, pady=5)

    # Creates a "+" button 
    Button(root, text="+", font=("Arial", 18), pady=15, padx=15, command="").grid(row=1, column=0, columnspan=3, pady=10)