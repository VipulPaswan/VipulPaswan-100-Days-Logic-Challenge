# Day 49 — Pancake Sorting in Python 🥞

Today I learned about Pancake Sorting — a unique sorting algorithm that works using only one operation: reversing (flipping) a prefix of the array.

---

## 🥞 What is Pancake Sorting?

Pancake Sorting is a comparison-based sorting algorithm where:
- The only allowed operation is reversing the first k elements
- No swapping of elements is allowed
- The idea is inspired by flipping pancakes with a spatula

---

## 🧠 Key Idea

To place the largest unsorted element at its correct position:
1. Flip it to the front
2. Flip it again to move it to the correct position

Repeat this process for smaller subarrays.

---

## 🔁 Allowed Operation

Only one operation is allowed:
- Reverse the array from index `0` to `k`

No direct swaps are used.

---

## 🧩 Example Concept

Unsorted array:
[3, 6, 1, 9, 4]

yaml
Copy code

Steps:
- Find largest element (9)
- Flip it to front
- Flip it to its correct position
- Reduce problem size

---

## ⚙️ Time Complexity

- Worst Case: **O(n²)**
- Space Complexity: **O(1)** (in-place)

---

## 🎯 Why Learn Pancake Sorting?

Even though it’s not used in real-world systems, Pancake Sorting:
- Improves logical thinking
- Teaches constraint-based problem solving
- Is commonly asked in coding interviews
- Strengthens understanding of sorting fundamentals

---

## 🏁 Summary

Pancake Sorting is a fun and creative algorithm that proves one thing clearly:
> Constraints force innovation.

Learning such algorithms builds stronger logic and problem-solving skills.
