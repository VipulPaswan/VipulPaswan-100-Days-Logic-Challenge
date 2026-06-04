# Day 66 — Memory Leaks & How to Avoid Them

Today I learned about memory leaks, their causes, and prevention techniques.

---

## 🧠 What is a Memory Leak?

A memory leak occurs when a program allocates memory but fails to release it even when it is no longer needed.

---

## ❗ Why Memory Leaks Are Dangerous

- Gradually consumes RAM  
- Slows down applications  
- Can crash long-running systems  
- Hard to detect  

---

## 🔍 Common Causes

- Open files not closed  
- Database connections not released  
- Unused objects still referenced  
- Unlimited caching  
- Global variables growing endlessly  

---

## 🛡 How to Prevent Memory Leaks

- Close all resources  
- Remove unused references  
- Limit cache size  
- Avoid unnecessary globals  
- Use scoped variables  

---

## 🏁 Summary

Preventing memory leaks is essential for building stable and scalable systems.
