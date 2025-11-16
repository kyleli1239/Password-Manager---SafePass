from tkinter import *
from tkinter import messagebox

def login_page(root):
    root.title("SafePass - Login Page")
    root.geometry("450x400")

    Label(root, text="Enter your Master Password", font=("Arial", 14)).pack(pady=10)

    # Create an entry box for the user to type the master password
    Entry(root, bg="Light Blue", width=30, font=("Arial", 14)).pack(pady=10)

    #Creates a submit button
    Button(root, text="Submit", pady=15, padx=15).pack()  # No command for now

if __name__ == "__main__":
    root = Tk()
    login_page(root)
    root.mainloop()