import tkinter as tk

def convert():
    try:
        value = float(entry_value.get())
        conversion = conversion_var.get()
        if conversion == "Meters to Feet":
            result_conv.set(value * 3.28084)
        elif conversion == "Celsius to Fahrenheit":
            result_conv.set((value * 9/5) + 32)
    except ValueError:
        result_conv.set("Invalid Input")

root = tk.Tk()
root.title("Unit Converter")

entry_value = tk.Entry(root)
entry_value.pack()
conversion_var = tk.StringVar(value="Meters to Feet")
tk.OptionMenu(root, conversion_var, "Meters to Feet", "Celsius to Fahrenheit").pack()
result_conv = tk.StringVar()
tk.Label(root, textvariable=result_conv).pack()
tk.Button(root, text="Convert", command=convert).pack()

root.mainloop()
