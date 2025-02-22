import tkinter as tk
from tkinter import messagebox

def submit_survey():
    selected_languages = [lang for lang, var in languages.items() if var.get()]
    experience_level = experience_var.get()
    result = f"You know: {', '.join(selected_languages) if selected_languages else 'None'}\n"
    result += f"Experience Level: {experience_level}"
    messagebox.showinfo("Survey Result", result)

root = tk.Tk()
root.title("Survey Form")

tk.Label(root, text="Which programming languages do you know?").pack(anchor="w")
languages = {"Python": tk.BooleanVar(), "Java": tk.BooleanVar(), "C++": tk.BooleanVar(), "JavaScript": tk.BooleanVar()}
for lang, var in languages.items():
    tk.Checkbutton(root, text=lang, variable=var).pack(anchor="w")

tk.Label(root, text="How experienced are you?").pack(anchor="w")
experience_var = tk.StringVar(value="Beginner")
for level in ["Beginner", "Intermediate", "Advanced"]:
    tk.Radiobutton(root, text=level, variable=experience_var, value=level).pack(anchor="w")

tk.Button(root, text="Submit", command=submit_survey).pack(pady=10)

root.mainloop()
