# Day 42 — Insert Data into MySQL Using Python (CREATE Operation)

Today I implemented the CREATE operation of CRUD by inserting records into a MySQL table using Python.

---

## 📌 What This Program Does

- Connects Python to MySQL  
- Creates an Employee object  
- Inserts employee data into the database  
- Commits changes permanently  
- Fetches and displays updated table records  

---

## 🧠 Key Concepts Used

### ✔ Employee Class
Represents a row in the employees table.

### ✔ INSERT Query
Adds a new record to the database.

### ✔ commit()
Saves changes permanently in MySQL.

### ✔ fetch after insert
Verifies whether insertion was successful.

---

## 🧩 Code Used (insert_employee.py)

```python
import mysql.connector

class Employee:
    def __init__(self, data):
        self.emp_id, self.emp_name, self.salary, self.department = data

def fetchEmployee(cursor):
    cursor.execute("select * from employees")
    return list(cursor)

def insertEmployee(cursor, emp):
    q = "INSERT INTO employees (emp_id, emp_name, salary, department) VALUES ({}, '{}', {}, '{}')".format(
        emp.emp_id, emp.emp_name, emp.salary, emp.department
    )
    cursor.execute(q)

def main():
    try:
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='xyz',
            database='db1'
        )

        if mydb.is_connected():
            print("connected to mysql Database")

        cursor = mydb.cursor()

        emp = Employee((13, 'Sunny', 25000000, 'sales'))
        insertEmployee(cursor, emp)
        mydb.commit()
        print("Record Inserted Successfully\n")

        employeedata = fetchEmployee(cursor)
        print("Employee Table:")
        for record in employeedata:
            print(record)

    except mysql.connector.Error as e:
        print("Error:", e)

    finally:
        if mydb.is_connected():
            cursor.close()
            mydb.close()
            print("\nConnection Closed")

if __name__ == '__main__':
    main()
📌 Example Output
css
Copy code
connected to mysql Database
Record Inserted Successfully

Employee Table:
(1, 'Vipul', 23000, 'IT')
(13, 'Sunny', 25000000, 'sales')

Connection Closed
🎯 Why This Matters?
INSERT operations allow applications to:

Store user data

Save transactions

Maintain records

Build real-world systems

This is a key backend milestone.

🔗 Next Steps
Update records using Python

Delete records using Python

Full CRUD App

GUI + Database integration

🏁 Summary
Day 42 helped me understand how Python inserts data into MySQL tables.