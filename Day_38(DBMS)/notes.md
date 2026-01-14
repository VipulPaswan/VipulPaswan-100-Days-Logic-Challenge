📄 Day 38 — DBMS & MySQL Basics

Today, I learned the fundamentals of DBMS (Database Management System) and MySQL, which form the backbone of almost every application—from web apps to mobile apps to desktop tools.

Understanding databases is essential for building real-world software.

🧠 What is DBMS?

A Database Management System is software used to store, manage, and retrieve data efficiently.

Examples:

MySQL

PostgreSQL

Oracle

SQL Server

SQLite

MongoDB (NoSQL)

🎯 Why Do We Need DBMS?

Stores data permanently

Prevents data duplication

Organizes data in tables

Ensures security & access control

Provides fast data retrieval

Supports large-scale applications

Maintains consistency, integrity, and accuracy

🏛 Database → Table → Rows → Columns

A database organizes information like this:

Database (SchoolDB)
→ Table: Students
→ Rows (student records)
→ Columns (name, age, marks)

📌 SQL vs MySQL
SQL	MySQL
A language to manage data	A DBMS that uses SQL
Syntax rules	Software to store & retrieve data
Works everywhere	One specific system
🧩 Important SQL Concepts
✔ Database

A container for tables.

✔ Table

Data stored in rows & columns.

✔ Primary Key

A unique identifier for each row.

✔ Foreign Key

Connects two tables (relationships).

✔ Query

Instruction to the database.

🧪 Basic SQL Commands I Learned

Create a database

CREATE DATABASE schoolDB;


Create a table

CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT
);


Insert data

INSERT INTO students VALUES (1, 'Vipul', 23);


Read data

SELECT * FROM students;


Update data

UPDATE students SET age = 24 WHERE id = 1;


Delete data

DELETE FROM students WHERE id = 1;

🔗 How This Connects to the Challenge

So far:

Day 32–37 → Tkinter GUI

Day 37 → Display data in a table

Day 38 → Learn DBMS (so that data can be stored permanently)

From GUI → Data → Database
Exactly how complete apps are built.

🏁 Summary

Learning DBMS is crucial for becoming a full-stack or backend developer.
I now understand:

What databases are

Why we use them

Basics of SQL

How MySQL stores and retrieves data

This sets the foundation for connecting Python + MySQL in the upcoming days.