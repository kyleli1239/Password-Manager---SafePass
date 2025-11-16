from tkinter import *
from tkinter import messagebox

def signup_page(root):
    root.title("SafePass - Signup Page")
    root.geometry("450x400")

    Label(root, text="Create New Master Password", font=("Arial", 14)).pack(pady=10)

    # Create an entry box for the user to type the master password
    Entry(root, bg="Light Blue", width=30, font=("Arial", 14)).pack(pady=10)

    #Creates a submit button
    Button(root, text="Submit", pady=15, padx=15).pack()  # No command for now

if __name__ == "__main__":
    root = Tk()
    signup_page(root)
    root.mainloop()

