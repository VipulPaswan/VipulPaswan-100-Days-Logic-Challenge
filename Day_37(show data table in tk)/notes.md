📄 Day 37 — Show Data in a Table using Tkinter (Treeview Widget)

Today I learned how to display structured data inside a table UI using Tkinter’s ttk.Treeview.
Treeview is an extremely useful widget for creating professional desktop applications that need tabular data.

🧠 Concepts Learned
✔ Treeview Widget

A table-like component from Tkinter's ttk module that supports:

Multiple columns

Headings

Custom column width

Row insertion

Scrollbars

Selection handling

✔ Column Configuration

Setting column names

Adjusting width

Center alignment

✔ Row Insertion

Dynamically adding tuples/lists into the table

Displaying structured product/data rows

📦 Features of This Project

Shows product details in a table

Clean & professional UI

Fully scrollable and interactive

Uses Tkinter + ttk for modern styling

Great for inventory, billing, records, admin dashboards

🧩 Code Used (table_view.py)
import tkinter as tk
from tkinter import ttk

# Columns
data_columns = ["Item ID", "Product Name", "Price (INR)", "Stock"]

# Sample Data
sample_data = [
    (101, "Wireless Mouse", 850, 45),
    (102, "Mechanical Keyboard", 4200, 15),
    (103, "USB-C Hub", 1500, 170),
    (104, "Laptop Stand", 990, 55),
    (105, "Monitor Cable", 450, 120)
]

def create_table_gui():
    root = tk.Tk()
    root.title("Data Table using Treeview")
    root.geometry("800x300")

    tree = ttk.Treeview(root, columns=data_columns, show='headings', height=10)

    # Define Columns
    for col in data_columns:
        tree.column(col, anchor=tk.CENTER, width=120)
        tree.heading(col, text=col)

    # Insert Rows
    for item in sample_data:
        tree.insert('', tk.END, values=item)

    # Grid placement
    tree.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_table_gui()

🏁 Summary

This project improved my understanding of how GUI apps display structured data.
Treeview is essential for developing:

Inventory management apps

Student record systems

Product dashboards

Admin tools

CRUD applications

A great step forward in my Tkinter + Python GUI journey!