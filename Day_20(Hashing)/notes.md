# Day 20 – Hashing & Hash Table in JavaScript

This folder contains my custom implementation of a Hash Table in JavaScript as part of my #100DaysLogicChallenge.  
Hashing is one of the most powerful concepts in DSA, enabling fast O(1) average-time lookups.

## What I Learned

### ✔ What is Hashing?
Hashing converts a key into a numerical index using a hash function, allowing direct access to values.

### ✔ Key Operations Implemented
- `set(key, value)` → Insert or update data  
- `get(key)` → Retrieve data in O(1)  
- `remove(key)` → Delete a key-value pair  
- `count()` → Number of stored items  
- Collision handling using **Separate Chaining**

### ✔ Hash Function
A simple ASCII-based hash function:
- Converts each character of key into ASCII  
- Sums them  
- Uses modulo to map into table size (`index = hash % table.length`)

### Example Inserted Data
Vipul → 94
Ashutosh → 92
Sunny → 95
Manu → 91
Satendra → 93


All values retrieved successfully.

## Why Hashing Matters
Hashing is widely used in:
- Maps / Dictionaries  
- Caching  
- Database Indexing  
- Compilers  
- Password Storage  
- File Systems  
- Blockchain  

Understanding hashing builds a strong foundation for high-performance systems.

## DSA Journey Connection
- Day 16 → Heap  
- Day 18 → Priority Queue  
- Day 19 → Set  
- **Day 20 → Hash Table**

## Files Included
Day_20/
│── hashing.js # HashTable implementation
│── notes.md # Concepts explained
│── README.md # This file



Continuing to strengthen logic & DSA fundamentals as part of the 100 Days Logic Challenge.
