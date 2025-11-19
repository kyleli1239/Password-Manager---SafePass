from tkinter import *
from tkinter import messagebox
from core.authentication import save_master_password
from GUI.login_window import login_page

def signup_page(root):
    root.title("SafePass - Signup Page")
    root.geometry("450x400")

    Label(root, text="Create New Master Password", font=("Arial", 14)).pack(pady=10)

    # Create an entry box for the user to type the master password
    master_password_entry = Entry(root, bg="Light Blue", width=30, font=("Arial", 14))
    master_password_entry.pack(pady=10)

    # Saves master password into database
    def submit_master_password():

        master_password = master_password_entry.get()

        # Validates the input
        if master_password.strip() == "":
            messagebox.showwarning("Error","Master Password cannot be empty")
    
        elif len(master_password) < 6: 
            messagebox.showwarning("Error","Master Password must be at least 6 characters long")

        # Once validated, uses function for authentication.py to store and hash the master password
        else:
            save_master_password(master_password)
            messagebox.showinfo("Success","Master Password created successfully")

            # Page is destroyed and login window opens
            root.destroy()
            new_root = Tk()
            login_page(new_root)

    # Creates a submit button. When clicked, calls submit_master_password()
    Button(root, text="Submit", pady=15, padx=15, command = submit_master_password).pack()