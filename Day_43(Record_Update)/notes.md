# Day 43 — Update Records in MySQL Using Python (UPDATE Operation)

Today I learned how to update existing records in a MySQL table using Python.  
This implements the UPDATE part of CRUD operations.

---

## 📌 What This Program Does

- Connects Python to MySQL  
- Identifies a record using `emp_id`  
- Updates employee name, salary, and department  
- Commits changes permanently  
- Closes database connection safely  

---

## 🧠 Key Concepts Used

### ✔ UPDATE Query
Modifies existing records in a table.

### ✔ WHERE Clause
Ensures only the intended record is updated.

### ✔ commit()
Saves the updated data permanently in the database.

### ✔ Object-Oriented Structure
Employee class represents a database row.

---

## 🧩 Code Used (update_employee.py)

```python
import mysql.connector

class Employee:
    def __init__(self, data):
        self.emp_id, self.emp_name, self.salary, self.department = data

def fetchEmployee(cursor):
    cursor.execute("select * from employees")
    return list(cursor)

def updateEmployee(cursor, emp):
    q = "UPDATE employees SET emp_name='{}', salary={}, department='{}' WHERE emp_id={}".format(
        emp.emp_name, emp.salary, emp.department, emp.emp_id
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

        emp = Employee((25, 'Vipul', 500000000, 'CEO'))
        updateEmployee(cursor, emp)
        mydb.commit()
        print("Record Updated Successfully")

    except mysql.connector.Error as e:
        print("Error:", e)

    finally:
        if mydb.is_connected():
            cursor.close()
            mydb.close()
            print("Connection Closed")

if __name__ == '__main__':
    main()

📌 Example Scenario

Before update:

(25, 'Vipul', 30000, 'Developer')


After update:

(25, 'Vipul', 500000000, 'CEO')

🎯 Why This Matters?

UPDATE operations allow applications to:

Modify user information

Change business data

Keep records up-to-date

Build dynamic, real-time systems

🔗 Next Steps

Delete records using Python

Combine CREATE + READ + UPDATE + DELETE

Build a complete Python CRUD application