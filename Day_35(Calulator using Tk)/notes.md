# Day 35 — Calculator Using Tkinter (Python GUI)

Today I built a functional calculator using Python’s Tkinter GUI library.  
This project covered:

- UI layout using grid  
- Button event handling  
- Expression evaluation  
- Input validation  
- Real-time screen updates  

---

## 🚀 Features
- Number buttons (0–9)  
- Operators (+, -, *, /)  
- Clear (AC)  
- Delete (DEL)  
- Decimal (.)  
- Equals (=)  
- Responsive UI layout

---

## 🧩 Tkinter Code (calculator.py)

```python
import tkinter as tk

def button_click(value):
    current = display.get()
    if current == "Error":
        display.delete(0, tk.END)

    display.insert(tk.END, value)

def clear_display():
    display.delete(0, tk.END)

def delete_last():
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current[:-1])

def calculate_result():
    try:
        expression = display.get()
        result = str(eval(expression))
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

root = tk.Tk()
root.title("Tkinter Calculator")
root.geometry("340x430")

display = tk.Entry(root, font=("Arial", 20), bd=5, relief=tk.RIDGE, justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

buttons = [
    ("7",1,0), ("8",1,1), ("9",1,2), ("/",1,3),
    ("4",2,0), ("5",2,1), ("6",2,2), ("*",2,3),
    ("1",3,0), ("2",3,1), ("3",3,2), ("-",3,3),
    ("0",4,0), (".",4,1), ("=",4,2), ("+",4,3),
]

for (text, row, col) in buttons:
    action = lambda x=text: button_click(x) if x != "=" else calculate_result()
    tk.Button(root, text=text, width=6, height=2,
              font=("Arial", 16), command=action)\
        .grid(row=row, column=col, padx=5, pady=5)

tk.Button(root, text="AC", width=6, height=2, font=("Arial", 16),
          command=clear_display).grid(row=5, column=0, padx=5, pady=5)

tk.Button(root, text="DEL", width=6, height=2, font=("Arial", 16),
          command=delete_last).grid(row=5, column=1, padx=5, pady=5)

root.mainloop()
