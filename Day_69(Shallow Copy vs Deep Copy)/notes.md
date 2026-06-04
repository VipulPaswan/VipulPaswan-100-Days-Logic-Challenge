# Day 69 — Shallow Copy vs Deep Copy

Today I studied how copying works in Python and why shallow and deep copies behave differently.

---

## 🧠 Shallow Copy

- Copies outer object only  
- Nested objects remain shared  
- Uses `copy()`  

---

## 🧠 Deep Copy

- Copies everything recursively  
- Nested objects are independent  
- Uses `deepcopy()`  

---

## 🎯 Why This Matters

- Prevents unintended data changes  
- Avoids hidden bugs  
- Makes programs predictable  

---

## 🏁 Summary

Shallow copy shares nested data.  
Deep copy creates independent data.