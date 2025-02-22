import tkinter as tk
import random

def show_quote():
    quotes = [
        "Believe in yourself!",
        "Never give up!",
        "Dream big and dare to fail!",
        "Success is not final, failure is not fatal."
    ]
    quote_var.set(random.choice(quotes))

root = tk.Tk()
root.title("Random Quote Generator")

quote_var = tk.StringVar()
tk.Label(root, textvariable=quote_var, wraplength=300).pack()
tk.Button(root, text="Show Quote", command=show_quote).pack()

root.mainloop()
