# Day 53 — Counting Sort

Today I learned Counting Sort, a non-comparison sorting algorithm that sorts numbers by counting digit frequency.

---

## 🧠 What is Counting Sort?

Counting Sort is a sorting algorithm where:
- Numbers are not compared directly  
- Instead, digit frequency is counted  
- Elements are placed directly into their sorted positions  

It is widely used in Radix Sort.

---

## 🔁 Core Steps

1. Create count array  
2. Count digit frequency  
3. Convert count to prefix sum  
4. Place values into output array  
5. Copy output to original array  

---

## ⚙️ Time & Space Complexity

| Metric | Value |
|-------|------|
| Time | **O(n + k)** |
| Space | **O(n + k)** |

---

## 🎯 When to Use

- Small range of integers  
- Sorting digits inside Radix Sort  
- Ranking systems  
- Counting frequency-based problems  

---

## ❌ When to Avoid

- Large unknown ranges  
- Memory-constrained systems  

---

## 🏁 Summary

Counting Sort proves that sorting doesn’t always require comparisons — sometimes counting is enough.

> Smart logic beats brute force.
