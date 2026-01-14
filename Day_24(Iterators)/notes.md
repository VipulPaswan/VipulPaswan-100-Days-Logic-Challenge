# Day 24 – Iterators in Python

An **iterator** in Python is an object that allows you to access elements of a collection **one at a time**, without needing to load everything at once. It is a core part of how loops, generators, file reading, and lazy evaluation work in Python.

---

## 📘 What is an Iterable?

An **iterable** is any object that can return an iterator.

Examples of iterables:
- list
- tuple
- string
- dictionary
- set
- file objects

These objects can be passed to `iter()`.

---

## 📘 What is an Iterator?

An **iterator** is an object with two special methods:
- `__iter__()` → returns the iterator object
- `__next__()` → returns the next value

When no items remain, `StopIteration` is raised.

---

## 🔍 Behind the Scenes of a For Loop

When we write:

```python
for x in li:
    print(x)


✔ What Happens Here?

iter(li) converts the list into an iterator

next(it) fetches values one by one

When items finish, StopIteration ends the loop

This is exactly how Python handles loops internally

🎯 Why Iterators Are Important?

Efficient for large data

Used in file reading (line by line)

Support lazy evaluation

Reduce memory usage

Foundation of generators and async streams

Common in backend pipelines and data processing

🧠 Summary

Iterators provide a powerful and memory-efficient way to access sequential data in Python.
Understanding them helps in mastering:

loops

generators

custom data structures

stream processing

backend systems