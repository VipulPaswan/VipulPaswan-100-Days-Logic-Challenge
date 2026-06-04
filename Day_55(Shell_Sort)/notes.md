# Day 55 — Shell Sort

Shell Sort is an optimized version of Insertion Sort that sorts elements using a gap method to improve efficiency.

---

## 🧠 What is Shell Sort?

Shell Sort sorts elements by comparing values that are far apart and gradually reduces the gap until it becomes 1.

This significantly reduces shifting operations.

---

## 🔁 Steps

1. Choose initial gap = n//2  
2. Compare and swap elements at gap distance  
3. Reduce gap  
4. Continue until gap becomes 1  

---

## ⚙️ Time Complexity

| Case | Complexity |
|----|-----------|
| Best | O(n log n) |
| Worst | O(n²) |

---

## 🎯 Why Use Shell Sort?

- Faster than insertion sort  
- Efficient for medium datasets  
- In-place sorting  
- No extra memory required  

---

## 🏁 Summary

Shell Sort improves insertion sort using smart gap logic, making sorting faster and more efficient.
