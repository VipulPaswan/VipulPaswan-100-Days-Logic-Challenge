# 📘 Day 31 — JSON (JavaScript Object Notation)

Today I learned JSON — the most widely used data format for storing and transferring data across applications, APIs, servers, and client systems. JSON is lightweight, readable, and supported by every major programming language, which makes it the backbone of modern software development.

---

## 🔍 What is JSON?

JSON stands for **JavaScript Object Notation**.  
It is a structured, text-based format used to represent data using:

- **Key–Value Pairs**
- **Objects (dictionaries-like)**
- **Arrays (lists-like)**
- **Strings, Numbers, Booleans, Null**

A JSON object looks like this:

```json
{
    "name": "Vipul",
    "age": 23,
    "skills": ["Python", "JavaScript", "Tailwind"],
    "isActive": true
}
⭐ Why JSON Is So Important?
📌 Most APIs return JSON (Weather API, YouTube API, GitHub API, etc.)

📌 Used in mobile apps, web apps, backend, cloud, databases

📌 Language-independent

📌 Lightweight and easy to understand

📌 Replaces XML in modern systems

📌 Perfect for configuration (.json), storage, authentication tokens

It is the universal medium through which systems talk to each other.

🧠 JSON in Python
Convert Python → JSON:
python
Copy code
import json
json_string = json.dumps(python_dict)
Convert JSON → Python:
python
Copy code
data = json.loads(json_string)
Read JSON file:
python
Copy code
with open("data.json") as f:
    data = json.load(f)
Write JSON file:
python
Copy code
with open("data.json", "w") as f:
    json.dump(mydata, f, indent=4)
🔗 Connected Learning Flow
Day 22 – XML: Understanding structured data

Day 23 – Reading XML with Python

Day 31 – JSON: Modern structured data (used by nearly all APIs)

JSON completes the transition from old-style XML → modern REST/HTTP API data format.

📌 Summary
Today I explored the fundamentals of JSON and how it simplifies data exchange between applications. JSON is one of the most essential concepts in web development, backend systems, APIs, and cloud services. Learning it brings me one step closer to API integrations and real-world backend development.