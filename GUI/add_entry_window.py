from tkinter import *
from tkinter import messagebox
from core.database import add_entry
from core.encryption import encrypt_text
import tkinter as tk

# Function displays the page which allows user to add entries into their vault
def add_entry_page(root,fernet):

    win = Toplevel(root)
    win.title("SafePass - Add new entry")
    win.geometry("400x300")

    Label(win, text="Enter Website").pack(pady=5)
    website_entry = Entry(win, bg="Light Blue", width=30)
    website_entry.pack()

    Label(win, text="Enter Username").pack(pady=5)
    username_entry = Entry(win, bg="Light Blue", width=30)
    username_entry.pack()

    Label(win, text="Enter Password").pack(pady=5)
    password_entry = Entry(win, bg="Light Blue", width=30)
    password_entry.pack()

    # Function to retrieve and pass the entries so they can be stored in the database.
    def save(): 

        # Temporarily disables button
        save_button.config(state=tk.DISABLED)
        
        website = website_entry.get()
        username = username_entry.get()
        password = password_entry.get()
        
        # Encrypts the website, username, password
        encrypted_website = encrypt_text(website, fernet)
        encrypted_username = encrypt_text(username, fernet)
        encrypted_password = encrypt_text(password, fernet)

        # Ensures none of the entries are empty
        if website == "" or username == "" or password == "":
            messagebox.showerror("Error", "All fields must be filled")
            save_button.config(state=tk.NORMAL)
            return
        
        # Stores entries in database
        # master_id always equals 1 as there is only 1 master password
        add_entry(1, encrypted_website, encrypted_username, encrypted_password)
        messagebox.showinfo("Success","Entry added successfully")

        win.destroy()

    # Save entry button. When clicked, calls the save function which stores the entries
    save_button = Button(win, text="Save Entry", command=save)
    save_button.pack(pady=15)
    return win