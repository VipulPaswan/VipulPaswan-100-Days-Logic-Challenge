# Day 47 — Python CRUD using SQLite

Today I built a simple CRUD-style application using Python and SQLite.  
SQLite is a lightweight, file-based database that requires no server setup.

---

## 🗄 What is SQLite?

SQLite is:
- Serverless  
- File-based  
- Zero configuration  
- Lightweight and fast  

It stores the entire database in a single `.db` file.

---

## 🚀 Features of This Program

- Automatic database connection  
- Table creation if not exists  
- Insert book records  
- View all book records  
- Menu-driven console interface  
- Safe query execution using placeholders  

---

## 🧠 Concepts Used

### ✔ sqlite3 module
Python’s built-in library for SQLite.

### ✔ Parameterized Queries
Prevents SQL injection and improves safety.

### ✔ AUTOINCREMENT
Automatically generates unique IDs.

### ✔ Menu-driven Logic
Allows continuous user interaction.

---

## 🧩 Program Flow

1. Connect to SQLite database  
2. Create table if not exists  
3. Show menu repeatedly  
4. Perform insert or view operation  
5. Exit and close database safely  

---

## 🧩 Code Used (book_crud.py)

```python
import sqlite3

DATABASE_NAME = 'book_records.db'

def connect_to_sqlite():
    try:
        con = sqlite3.connect(DATABASE_NAME)
        print("Database connection established")
        return con
    except Exception as e:
        print("Error connecting to database:", e)
        return None

def create_table(con):
    q = """
    CREATE TABLE IF NOT EXISTS book (
        book_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        price REAL
    )
    """
    cur = con.cursor()
    cur.execute(q)
    con.commit()

def insert_record(con):
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    price = float(input("Enter price: "))

    q = "INSERT INTO book (title, author, price) VALUES (?, ?, ?)"
    cur = con.cursor()
    cur.execute(q, (title, author, price))
    con.commit()

def view_records(con):
    q = "SELECT * FROM book"
    cur = con.cursor()
    cur.execute(q)
    records = cur.fetchall()

    if records:
        for row in records:
            print(row)
    else:
        print("No records found")

def main():
    con = connect_to_sqlite()
    if not con:
        return

    create_table(con)

    while True:
        print("\n1. Insert Book")
        print("2. View Books")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            insert_record(con)
        elif choice == '2':
            view_records(con)
        elif choice == '3':
            break
        else:
            print("Invalid choice")

    con.close()
    print("Database connection closed")

if __name__ == '__main__':
    main()