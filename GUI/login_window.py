from tkinter import *
from tkinter import messagebox
from core.authentication import authenticate_master_password
from GUI.vault_window import vault_page

def login_page(root):
    root.title("SafePass - Login Page")
    root.geometry("450x400")

    Label(root, text="Enter your Master Password", font=("Arial", 14)).pack(pady=10)

    # Create an entry box for the user to type the master password
    password_entry = Entry(root, bg="Light Blue", width=30, font=("Arial", 14))
    password_entry.pack(pady=10)

    # Calls the authenticate_master_password function from authentication.py
    def check_password():
        entered_password = password_entry.get()

        key = authenticate_master_password(entered_password)

        # If the key is present, the passwords match and user is authenticated
        if key:
            messagebox.showinfo("Success","Login Successful")

            # Page is destroyed and vault window opens
            root.destroy()
            new_root = Tk()
            vault_page(new_root,key) # Key is passed to the vault page

        else:
            messagebox.showerror("Error","Login failed. Incorrest master password")

    # Creates a submit button. When clicked, calls the function authenticate_master_password 
    Button(root, text="Submit", pady=15, padx=15, command=check_password).pack()
