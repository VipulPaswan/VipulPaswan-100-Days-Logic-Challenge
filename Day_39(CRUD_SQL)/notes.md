# Day 39 — CRUD Operations (Create, Read, Update, Delete)

CRUD represents the four basic actions performed on database data.  
Every major application uses CRUD at its core.

---

## 🔥 What is CRUD?

### 1️⃣ CREATE — Insert new record
Adds new data into a table.

Example:
```sql
INSERT INTO students (id, name, age) VALUES (1, 'Vipul', 23);
2️⃣ READ — Retrieve data
Fetch data from the table.

Example:

sql
Copy code
SELECT * FROM students;
3️⃣ UPDATE — Modify an existing record
Changes data inside a row.

Example:

sql
Copy code
UPDATE students SET age = 24 WHERE id = 1;
4️⃣ DELETE — Remove a record
Deletes specific data.

sql
Copy code
DELETE FROM students WHERE id = 1;
🧠 Why CRUD is Important?
Used in every app (Instagram posts, YouTube videos, login systems)

Core of backend development

Essential for building APIs

Required for database integration with Python, JavaScript, etc.

Helps create real-world applications like:

Billing systems

Student management

Employee records

Inventory systems

🔗 Connection to Previous Days
Day 38 → DBMS & MySQL basics

Day 39 → CRUD fundamentals

Next → Python + MySQL CRUD Application

🏁 Summary
Understanding CRUD means understanding how real applications store, read, modify, and delete data.
This is the backbone of backend development and the next step toward full projects.