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
    print("Table created or already exists")


def insert_record(con):
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    price = float(input("Enter price: "))

    q = "INSERT INTO book (title, author, price) VALUES (?, ?, ?)"
    cur = con.cursor()
    cur.execute(q, (title, author, price))
    con.commit()
    print("Book record inserted successfully")


def view_records(con):
    q = "SELECT * FROM book"
    cur = con.cursor()
    cur.execute(q)
    records = cur.fetchall()

    if not records:
        print("No records found")
    else:
        print("\nBook Records:")
        print("ID | Title | Author | Price")
        print("-" * 40)
        for row in records:
            print(row)


def main():
    con = connect_to_sqlite()
    if not con:
        return

    create_table(con)

    while True:
        print("\n--- Book Management Menu ---")
        print("1. Insert Book")
        print("2. View Books")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            insert_record(con)
        elif choice == '2':
            view_records(con)
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice")

    con.close()
    print("Database connection closed")


if __name__ == '__main__':
    main()
