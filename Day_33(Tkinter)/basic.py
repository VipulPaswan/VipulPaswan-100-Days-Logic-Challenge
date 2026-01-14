import tkinter as tk

def show_greeting():
    name = name_entry.get()
    if name.strip() == "":
        result_label.config(text="Please enter your name!")
    else:
        result_label.config(text=f"Hello, {name}! Welcome 😊")

# main window
root = tk.Tk()
root.title("Greeting App")
root.geometry("350x200")
root.config(bg="#f0f0f0")

# label
tk.Label(root, text="Enter your name:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)

# entry
name_entry = tk.Entry(root, font=("Arial", 12))
name_entry.pack(pady=5)

# button
tk.Button(root, text="Greet Me", font=("Arial", 12), bg="#4CAF50", fg="white",
          command=show_greeting).pack(pady=10)

# output label
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="#f0f0f0")
result_label.pack(pady=10)

root.mainloop()
