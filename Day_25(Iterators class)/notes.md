# Day 25 – Custom Iterable & Iterator in Python

Today I learned how to create custom **iterable and iterator classes** in Python.  
Instead of using built-in iteration (list/tuple), I implemented my own iteration logic — which helped me understand what happens behind every `for` loop.

---

## 🔍 What I Learned

### ✔ Iterable
An object is iterable if it has:

```python
__iter__()


It must return an iterator object.

✔ Iterator

Iterator must implement:

__next__()


Every next() returns the next value.
When no items remain → StopIteration is raised.

This is exactly how for i in object: works internally.

🧪 What I Built

1️⃣ Counter Iterable

Behaves like range(start, end)

Generates numbers one by one

Stops when end is reached

2️⃣ Integer Iterable

Converts a number into digits

Example: 1234 → 1, 2, 3, 4

Each digit yielded on iteration

Both custom classes can now be used inside loops just like Python's built-in iterables.

🎯 Why This Is Important

Learned inner mechanism of iteration

Built iteration instead of just using it

Foundation before learning Generators

Essential for data streaming & large datasets

Used in backend pipelines & object-based iteration

🔗 Learning Flow (Past 3 Days)

Day 23 → XML Parsing using Python

Day 24 → Iterators (Basics)

Day 25 → Custom Iterables + Custom Iterators

Concepts are building step-by-step —
from using iteration → understanding → implementing it.