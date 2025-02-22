import tkinter as tk

def change_color():
    root.configure(bg=color_var.get())

root = tk.Tk()
root.title("Theme Customization")

color_var = tk.StringVar(value="white")
tk.OptionMenu(root, color_var, "white", "blue", "green", "yellow", "red", command=lambda _: change_color()).pack()

root.mainloop()
