import mysql.connector


class Employee:
    def __init__(self,data):
        self.emp_id,self.emp_name,self.salary,self.department = data


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

def deleteEmployee(cursor,emp_id):
    q="delete from employees where emp_id={}".format(emp_id)
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
        while True:
            print("\n1. Insert Employee")
            print("2. View Employees")
            print("3. Update Employee")
            print("4. Delete Employee")
            print("5. Exit")

            choice = int(input("Enter choice: "))
            if(choice==1):
                # INSERT FIRST
                    emp = Employee((
                        int(input("Emp ID: ")),
                        input("Name: "),
                        int(input("Salary: ")),
                        input("Department: ")
                    ))
                    insertEmployee(cursor, emp)
                    mydb.commit()
                    print("Record Inserted Successfully\n")
                    
            elif choice == 2:
                data = fetchEmployee(cursor)
                for row in data:
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
                print("Updated")
        
            elif choice == 4:
                emp_id = int(input("Emp ID to delete: "))
                deleteEmployee(cursor, emp_id)
                mydb.commit()
                print("Deleted")
        
            elif choice == 5:
                break
                 
    except mysql.connector.Error as e:
        print("Error:", e)

    finally:
        if mydb.is_connected():
            cursor.close()
            mydb.close()
            print("\nConnection Closed")
      
if __name__ == '__main__':
    main()

    
