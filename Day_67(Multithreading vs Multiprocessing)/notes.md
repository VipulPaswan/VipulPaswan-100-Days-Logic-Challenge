# Day 67 — Multithreading vs Multiprocessing

Today I studied how programs perform tasks in parallel using threads and processes.

---

## 🧵 Multithreading

- Multiple threads in a single process  
- Share same memory  
- Best for I/O-bound tasks  
- Faster communication  
- Limited by Python GIL  

---

## 🧱 Multiprocessing

- Multiple processes with independent memory  
- True parallelism  
- Best for CPU-bound tasks  
- Safer memory isolation  

---

## 🎯 When to Use

| Use Case | Best Choice |
|--------|-----------|
| File handling | Multithreading |
| Network requests | Multithreading |
| Heavy calculations | Multiprocessing |

---

## 🏁 Summary

Threads share memory.  
Processes share nothing.  
Choose wisely based on workload.
