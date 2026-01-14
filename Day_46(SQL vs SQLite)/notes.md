# Day 46 — MySQL vs SQLite: Which Database Should You Use?

Today I compared two popular relational databases — MySQL and SQLite — to understand their use cases, strengths, and limitations.

---

## 🗄 What is MySQL?

MySQL is a **server-based relational database** used widely in production systems.

### Key Features:
- Client–server architecture  
- Supports multiple users  
- High performance  
- Scalable  
- Used in web applications  
- Requires installation and configuration  

### Common Use Cases:
- Web applications  
- Enterprise systems  
- Large-scale projects  
- Backend APIs  

---

## 🗂 What is SQLite?

SQLite is a **file-based database** stored as a single `.db` file.

### Key Features:
- No server required  
- Zero configuration  
- Lightweight  
- Embedded database  
- Extremely fast for small apps  

### Common Use Cases:
- Desktop applications  
- Mobile apps (Android, iOS)  
- Prototypes & testing  
- Small local tools  

---

## ⚖ MySQL vs SQLite (Conceptual Comparison)

- MySQL → Server-based, scalable, multi-user  
- SQLite → File-based, lightweight, single-user focused  

---

## 🎯 Which One Should You Choose?

Choose **MySQL** if:
- You are building web apps  
- Multiple users access data  
- You need scalability  

Choose **SQLite** if:
- You are building a small app  
- You want zero setup  
- You need fast local storage  

---

## 🏁 Summary

There is no “best” database — only the **right database for the right problem**.  
Understanding when to use MySQL or SQLite helps build efficient, maintainable applications.

This knowledge strengthens backend decision-making skills.
