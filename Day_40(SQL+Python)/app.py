import mysql.connector
mydb = None
cursor = None

try:
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='xyz',
        database='db1'
    )

    if mydb.is_connected():
        print("Connected to MySQL database")
        cursor = mydb.cursor()
        cursor.execute("show databases")
        for x in cursor:
            print(x)

    else:
        print("Not connected to MySQL database")

except mysql.connector.Error as e:
    print("Error connecting MySQL:", e)

finally:
    if cursor is not None:
        cursor.close()
    if mydb is not None and mydb.is_connected():
        mydb.close()
        print("MySQL connection closed")


