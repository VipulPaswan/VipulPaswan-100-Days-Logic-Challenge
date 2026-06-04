# Day 65 — Garbage Collection & Memory Cleanup

Today I learned how programs automatically free unused memory using garbage collection.

---

## 🧠 What is Garbage Collection?

Garbage Collection is a process that removes unused objects from heap memory to free space and prevent memory leaks.

---

## 🔁 How GC Works

1. Program creates objects in heap  
2. GC tracks object references  
3. Unreachable objects are marked as garbage  
4. Memory is cleaned automatically  

---

## 🧩 Live vs Dead Objects

- Live Objects → Still reachable by program  
- Dead Objects → No longer used, eligible for cleanup  

---

## 🎯 Why Garbage Collection Matters

- Prevents memory leaks  
- Keeps applications stable  
- Reduces crashes  
- Makes memory handling easier  

---

## 🏁 Summary

Garbage collection keeps programs clean, efficient, and stable without manual memory management.
