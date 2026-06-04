# Day 44 — Delete Records in MySQL Using Python (DELETE Operation)

Today I implemented the DELETE operation of CRUD using Python and MySQL.  
This allows removing specific records from a database table safely.

---

## 📌 What This Program Does

- Connects Python to MySQL  
- Deletes an employee record using `emp_id`  
- Commits the deletion permanently  
- Closes database connection properly  

---

## 🧠 Key Concepts Used

### ✔ DELETE Query
Removes a specific row from the table.

### ✔ WHERE Clause
Ensures only the targeted record is deleted.

### ✔ commit()
Makes sure deletion is saved permanently.

### ✔ Full CRUD Completion
This final step completes Create, Read, Update, and Delete.

---

## 🧩 Code Used (delete_employee.py)

```python
import mysql.connector

class Employee:
    def __init__(self, data):
        self.emp_id, self.emp_name, self.salary, self.department = data

def deleteEmployee(cursor, emp_id):
    q = "DELETE FROM employees WHERE emp_id={}".format(emp_id)
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

        deleteEmployee(cursor, emp_id=25)
        mydb.commit()
        print("Record Deleted Successfully")

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
Before delete:

bash
Copy code
(25, 'Vipul', 500000000, 'CEO')
After delete:

pgsql
Copy code
Record removed from table
🎯 Why This Matters?
DELETE operations help applications:

Maintain clean databases

Remove invalid data

Manage user accounts

Control storage growth

🏁 Summary
Day 44 completed the full CRUD cycle using Python and MySQL.
I can now create, read, update, and delete database records programmatically — a major backend milestone.

yaml
Copy code
