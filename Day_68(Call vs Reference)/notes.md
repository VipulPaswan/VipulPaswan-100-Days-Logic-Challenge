# Day 68 — Does Python Use Call by Value or Call by Reference?

Today I learned how Python actually passes arguments to functions.

---

## 🧠 The Truth

Python uses **Call by Object Reference**.

It passes a reference to the object, not a copy and not a raw memory pointer.

---

## 🔁 Mutable vs Immutable

| Type | Behavior |
|----|---------|
| int, float, str, tuple | Behave like call by value |
| list, dict, set | Behave like call by reference |

---

## 🎯 Why This Matters

- Prevents unintended data changes  
- Makes debugging easier  
- Builds strong Python fundamentals  

---

## 🏁 Summary

Python does not use call by value or reference — it uses **call by object reference**.
