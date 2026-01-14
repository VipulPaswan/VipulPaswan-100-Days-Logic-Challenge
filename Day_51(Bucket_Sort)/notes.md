# Day 51 — Bucket Sort

Today I learned about Bucket Sort, a distribution-based sorting algorithm that works by dividing elements into buckets and sorting them individually.

---

## 🧠 What is Bucket Sort?

Bucket Sort is a sorting technique where:
- Elements are distributed into multiple buckets
- Each bucket is sorted separately
- Buckets are merged to form the final sorted list

It works best when input data is uniformly distributed.

---

## 🔁 Core Idea

Instead of comparing elements repeatedly:
1. Group elements into buckets based on range
2. Sort each group
3. Combine results

This reduces unnecessary comparisons.

---

## ⚙️ Time & Space Complexity

- Best / Average Case: **O(n + k)**
- Worst Case: **O(n²)**
- Space Complexity: **O(n + k)**

Where:
- `n` = number of elements  
- `k` = number of buckets  

---

## ✅ When to Use Bucket Sort

- Floating point numbers  
- Scores / percentages  
- Uniformly distributed data  
- Known data range  

---

## ❌ When to Avoid

- Highly skewed data  
- Unknown data distribution  
- Very small datasets  

---

## 🎯 Key Takeaway

Bucket Sort shows that understanding your data is just as important as choosing the algorithm.

> Right algorithm + right data = efficient solution

---

## 🏁 Summary

Day 51 helped me understand how sorting can be optimized using data distribution rather than pure comparisons.  
This strengthens algorithmic thinking and decision-making.