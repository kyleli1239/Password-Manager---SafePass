from tkinter import *
from tkinter import messagebox
from core.database import add_entry

# Function displays the page which allows user to add entries into their vault
def add_entry_page(root):

    root = Toplevel(root)
    root.title("SafePass - Add new entry")
    root.geometry("400x300")

    Label(root, bg="Light Blue", text="Enter Website").pack(pady=5)
    website_entry = Entry(root,width=30)
    website_entry.pack()

    Label(root, bg="Light Blue", text="Enter Username").pack(pady=5)
    username_entry = Entry(root,width=30)
    username_entry.pack()

    Label(root,  bg="Light Blue", text="Enter Password").pack(pady=5)
    password_entry = Entry(root,width=30)
    password_entry.pack()

    # Function to retrieve and pass the entries so they can be stored in the database.
    def save():
        website = website_entry.get()
        username = username_entry.get()
        password = password_entry.get()

        # Ensures none of the entries are empty
        if website == "" or username == "" or password == "":
            messagebox.showerror("Error", "All fields must be filled")
            return
        
        # Stores entries in database
        # master_id always equals 1 as there is only 1 master password
        add_entry(1, website, username, password)
        messagebox.showinfo("Success","Entry added successfully")

        root.destroy()

    # Save entry button. When clicked, calls the save function which stores the entries
    Button(root, text="Save Entry", command=save).pack(pady=15)