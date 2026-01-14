import mysql.connector


def fetchEmployee(cursor):
    cursor.execute("select * from employees")
    return list(cursor)
    

def main():
    try:
        mydb = mysql.connector.connect(host = 'localhost',
                                       user = 'root',
                                       password = 'xyz',
                                       database = 'db1'
                                       )
        if mydb.is_connected():
            print("connected to mysql Database")
            cursor = mydb.cursor()
            employeedata=fetchEmployee(cursor)
            for record in employeedata:
                print(record)
            
        else:
            print("Connection Failed")
    
    except mysql.connector.Error as e:
        print("Error: ",e)
        
    finally:
        if mydb.is_connected():
            cursor.close()
            mydb.close()
            print("Connection Closed")
            
if __name__ == '__main__':
    main()

    