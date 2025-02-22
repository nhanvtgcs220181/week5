import tkinter as tk
from tkinter import messagebox

def login():
    email = email_entry.get()
    password = password_entry.get()
    if email == "admin@test.com" and password == "Greenwich@123":
        messagebox.showinfo("Login", "Login Successful")
    else:
        messagebox.showerror("Login", "Invalid Login")

def toggle_password():
    if password_entry.cget("show") == "*":
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

root = tk.Tk()
root.title("Login Form")

email_entry = tk.Entry(root)
email_entry.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()
tk.Button(root, text="Show/Hide", command=toggle_password).pack()
tk.Button(root, text="Login", command=login).pack()

root.mainloop()
