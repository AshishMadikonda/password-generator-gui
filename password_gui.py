import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())

    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = ''.join(
        random.choice(characters)
        for _ in range(length)
    )

    result_label.config(text=password)

    if length < 8:
        strength_label.config(text="Strength: Weak")
    elif length < 12:
        strength_label.config(text="Strength: Medium")
    else:
        strength_label.config(text="Strength: Strong")

def copy_password():
    password = result_label.cget("text")

    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()

root = tk.Tk()
root.configure(bg="#222222")
root.title("Password Generator")
root.geometry("400x300")

title_label = tk.Label(
    root,
    text="Password Generator",
    font=("Arial", 16),
    bg="#222222",
    fg="white"
)
title_label.pack(pady=10)

length_entry = tk.Entry(root)
length_entry.pack(pady=10)
length_entry.insert(0, "12")

generate_button = tk.Button(
    root,
    text="Generate Password",
    command=generate_password
)
generate_button.pack(pady=10)

copy_button = tk.Button(
    root,
    text="Copy Password",
    command=copy_password
)
copy_button.pack(pady=5)

result_label = tk.Label(
    root,
    text="Your password will appear here",
    wraplength=350
)
result_label.pack(pady=20)

strength_label = tk.Label(
    root,
    text="Strength: "
)
strength_label.pack(pady=5)
root.mainloop()