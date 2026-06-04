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
        '''
        # INSERT FIRST
        emp = Employee((13, 'Sunny', 25000000, 'sales'))
        insertEmployee(cursor, emp)
        mydb.commit()
        print("Record Inserted Successfully\n")
        '''
        '''
        FETCH AFTER INSERT
        employeedata = fetchEmployee(cursor)
        print("Employee Table:")
        for record in employeedata:
            print(record)
        '''
            
        # UPDATE RECORD
        emp = Employee((25,'Vipul',500000000,'CEO'))
        updateEmployee(cursor,emp)
        mydb.commit()
        

    except mysql.connector.Error as e:
        print("Error:", e)

    finally:
        if mydb.is_connected():
            cursor.close()
            mydb.close()
            print("\nConnection Closed")

            
if __name__ == '__main__':
    main()

    
