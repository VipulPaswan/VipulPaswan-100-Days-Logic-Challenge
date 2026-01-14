# Day 26 – Generators in Python (Prime Number Generator)

Today I learned about **Generators** in Python and implemented a Prime Number Generator using `yield`.  
Generators allow us to produce values lazily — one at a time — instead of generating everything at once.  
This makes them extremely memory-efficient, especially for large sequences.

---

## 🔍 What is a Generator?

A generator is a special type of function that:

- Uses `yield` instead of `return`
- Produces values one-by-one
- Does not store the entire result in memory
- Stops automatically when values finish

Generators are basically **iterators with simpler syntax and better performance**.

---

## 💡 Why Generators Are Useful

- Handle large data efficiently  
- Reduce memory consumption  
- Fast execution due to lazy evaluation  
- Used in file reading, data streaming, pipelines, APIs  

Generators are a major upgrade from normal functions or custom iterators.

---

## 🧪 Code – Prime Number Generator with `yield`

```python
def isPrime(n):
    for i in range(2,n):
        if(n%i==0):
            return False  
    return True


def nextPrime(n):
    while not isPrime(n:=n+1):
        pass
    return n

def primeGenerator(n):
    x = 2
    while n:
        if(isPrime(x)):
            n = n-1
            yield x
        x = nextPrime(x)

prime_list = [num for num in primeGenerator(10)]
print(prime_list)

