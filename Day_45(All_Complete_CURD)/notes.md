# Day 45 — Complete Python CRUD Application using MySQL

Today I built a complete menu-driven CRUD application using Python and MySQL.  
This project integrates Create, Read, Update, and Delete operations in a single program.

---

## 🚀 Features

- Insert new employee records  
- View all employees  
- Update employee details  
- Delete employee records  
- Menu-driven console interface  
- Uses MySQL for permanent data storage  

---

## 🧠 Concepts Used

### ✔ Object-Oriented Programming
Employee class represents database records.

### ✔ CRUD Operations
- CREATE → Insert employee  
- READ → View employees  
- UPDATE → Modify employee details  
- DELETE → Remove employee  

### ✔ Database Handling
- mysql-connector-python  
- commit() for saving data  
- Proper connection closing  

---

## 🧩 Program Flow

1. Connect Python to MySQL  
2. Display menu repeatedly  
3. Perform operation based on user choice  
4. Commit database changes  
5. Exit safely  

---

## 🧩 Code Used (crud_app.py)

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

def updateEmployee(cursor, emp):
    q = "UPDATE employees SET emp_name='{}', salary={}, department='{}' WHERE emp_id={}".format(
        emp.emp_name, emp.salary, emp.department, emp.emp_id
    )
    cursor.execute(q)

def deleteEmployee(cursor, emp_id):
    q = "DELETE FROM employees WHERE emp_id={}".format(emp_id)
    cursor.execute(q)

def main():
    try:
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Vipul@123456789',
            database='db1'
        )

        cursor = mydb.cursor()

        while True:
            print("\n1. Insert Employee")
            print("2. View Employees")
            print("3. Update Employee")
            print("4. Delete Employee")
            print("5. Exit")

            choice = int(input("Enter choice: "))

            if choice == 1:
                emp = Employee((
                    int(input("Emp ID: ")),
                    input("Name: "),
                    int(input("Salary: ")),
                    input("Department: ")
                ))
                insertEmployee(cursor, emp)
                mydb.commit()
                print("Inserted Successfully")

            elif choice == 2:
                for row in fetchEmployee(cursor):
                    print(row)

            elif choice == 3:
                emp = Employee((
                    int(input("Emp ID to update: ")),
                    input("New Name: "),
                    int(input("New Salary: ")),
                    input("New Department: ")
                ))
                updateEmployee(cursor, emp)
                mydb.commit()
                print("Updated Successfully")

            elif choice == 4:
                emp_id = int(input("Emp ID to delete: "))
                deleteEmployee(cursor, emp_id)
                mydb.commit()
                print("Deleted Successfully")

            elif choice == 5:
                break

    except mysql.connector.Error as e:
        print("Error:", e)

    finally:
        cursor.close()
        mydb.close()
        print("Connection Closed")

if __name__ == '__main__':
    main()
🏁 Summary
Day 45 represents a major milestone in my backend journey.
I successfully built a complete CRUD application using Python and MySQL — a real-world foundation for backend development.