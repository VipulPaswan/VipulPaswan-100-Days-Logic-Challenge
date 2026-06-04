# Day 74 — Python del Keyword EXPOSED

Today I learned that the `del` keyword does not delete objects directly — it removes references.

---

## 🧠 What del Actually Does

- Removes a variable reference  
- Object remains if other references exist  
- Memory is freed only when reference count becomes zero  

---

## 🔁 When Object Is Really Deleted

- All references must be removed  
- Garbage collector frees memory  

---

## 🎯 Why This Matters

- Prevents memory misunderstanding  
- Avoids bugs  
- Improves system-level thinking  

---

## 🏁 Summary

`del` deletes names, not objects.
