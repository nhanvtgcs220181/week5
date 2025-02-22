import tkinter as tk

def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if operation == "+":
            result_var.set(num1 + num2)
        elif operation == "-":
            result_var.set(num1 - num2)
        elif operation == "*":
            result_var.set(num1 * num2)
        elif operation == "/":
            result_var.set(num1 / num2 if num2 != 0 else "Error")
    except ValueError:
        result_var.set("Invalid Input")

root = tk.Tk()
root.title("Simple Calculator")

entry1 = tk.Entry(root)
entry1.pack()
entry2 = tk.Entry(root)
entry2.pack()
result_var = tk.StringVar()
tk.Label(root, textvariable=result_var).pack()

for op in ["+", "-", "*", "/"]:
    tk.Button(root, text=op, command=lambda o=op: calculate(o)).pack(side="left")

root.mainloop()
