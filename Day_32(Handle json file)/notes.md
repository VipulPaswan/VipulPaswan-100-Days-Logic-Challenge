# Day 32 — Handling JSON File in JavaScript (Node.js)

Today I learned how to work with JSON files using Node.js. JSON is the most widely used data format in modern web development, and handling it properly is essential for backend, APIs, and data processing.

---

## 📌 Sample JSON (sample.json)

```json
{
    "name": "KL Rahul",
    "age": 32,
    "is_active": true,
    "client": {
        "id": "kl01",
        "username": "rahul01"
    },
    "score": [199, 50, 100, 97, 85]
}
📌 JavaScript Code (handle_json.js)
javascript
Copy code
try {
    const data = require('./sample.json');

    console.log(data['name']); // Direct access

    for (key in data) {
        if (typeof data[key] !== 'object') {
            console.log(key, '-', data[key]);
        }
        else if (data[key] instanceof Array) {
            const arr = data[key];

            if (typeof arr[0] !== 'object') {
                for (e of arr) {
                    console.log(e);
                }
            } else {
                for (e of arr) {
                    for (k1 in e) {
                        console.log(k1, ' - ', e[k1]);
                    }
                }
            }
        }
    }

} catch (error) {
    console.log("Error:", error);
}
📌 Output
nginx
Copy code
KL Rahul
name - KL Rahul
age - 32
is_active - true
199
50
100
97
85
⭐ What This Taught Me
How Node.js automatically parses JSON

How to differentiate between:

Primitive value

Object

Array

How to loop through JSON dynamically

How APIs return nested structured data

🔗 Connected Learning
Day 31 → JSON Basics

Day 32 → Handling JSON in JavaScript

Next → JSON + API Integration (real-world use)

🏁 Summary
JSON handling is a core skill for any backend or full-stack developer. Today’s session helped me understand dynamic extraction of values, nested structures, and arrays — exactly how real APIs work.

yaml
Copy code
