# Day 60 — Recursion Problems Practice

Today I focused on strengthening recursion concepts by practicing recursive problem-solving and understanding how recursive calls work internally.

---

## 🧠 What is Recursion?

Recursion is a programming technique where a function calls itself to solve smaller versions of the same problem until a base condition is met.

---

## 🧩 Two Core Parts of Recursion

Every recursive function must have:

### 1. Base Case  
The condition where recursion stops.

Without a base case, recursion will run infinitely and crash the program.

### 2. Recursive Case  
The part where the function calls itself with a smaller or simpler input.

---

## 🔁 How Recursion Works Internally

- Each function call is stored in the **call stack**
- The function keeps calling itself until the base case is reached
- Then the stack starts returning values step by step

This process is called **stack unwinding**.

---

## 🎯 Why Recursion is Important

- Used in tree and graph traversal  
- Helps in divide & conquer algorithms  
- Used in backtracking problems  
- Makes complex problems simpler  
- Improves logical thinking  

---

## ⚠️ Common Recursion Mistakes

- Missing base case  
- Incorrect base condition  
- Not reducing problem size  
- Causing stack overflow  

---

## 🏁 Summary

Recursion teaches us to break problems into smaller self-similar problems and build solutions step by step.

> If you can solve the smallest case, you can solve the whole problem.
