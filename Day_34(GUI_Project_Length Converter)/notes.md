# Day 34 — Length Converter App Using Tkinter

Today I built a simple GUI-based Length Converter using Python's Tkinter library. The app converts a value (in centimeters) to **meters** and **kilometers**.

This project helped revise:
- Tkinter widgets  
- Input handling  
- Event-driven logic  
- Real-time UI updates  

---

## 🚀 Features
- User enters a length in centimeters  
- Convert button calculates:
  - Meters  
  - Kilometers  
- Shows output immediately  
- Handles invalid inputs (non-numeric entries)

---

## 🧩 Tkinter Code (length_converter.py)

```python
import tkinter as tk

def convert_length():
    try:
        cm = float(entry.get())
        meters = cm / 100
        kilometers = cm / 100000

        result_label.config(
            text=f"Meters: {meters:.3f}\nKilometers: {kilometers:.6f}",
            fg="green"
        )
    except ValueError:
        result_label.config(text="Please enter a valid number!", fg="red")

root = tk.Tk()
root.title("Length Converter")
root.geometry("350x250")
root.config(bg="#f2f2f2")

title = tk.Label(root, text="Length Converter (cm → m, km)", font=("Arial", 14, "bold"), bg="#f2f2f2")
title.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 12), width=20)
entry.pack(pady=5)

convert_btn = tk.Button(root, text="Convert", font=("Arial", 12), bg="#4CAF50", fg="white", command=convert_length)
convert_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), bg="#f2f2f2")
result_label.pack(pady=10)

root.mainloop()


🏁 Summary

This small Tkinter project helped reinforce GUI concepts and logical thinking. Converters, calculators, and form-based apps are great stepping-stones for bigger desktop applications.