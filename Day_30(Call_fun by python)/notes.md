# Day 30 — Calling C Code from Python using DLL + ctypes

Today I learned how to run C functions directly inside Python by converting the `.c` file into a `.dll` file and loading it using `ctypes`.  
This gives us **C performance + Python simplicity.**

---

## 🧠 Concept Summary

| C Role | Python Role |
|-------|-------------|
| High performance computation | Interface + Execution control |
| Faster loops, math, memory access | Easy input/output handling |
| Creates DLL library | Loads DLL + calls functions |

Python becomes the manager, C becomes the worker.

---

## 📌 Step 1 — Create C Source File

`customlib.c`

```c
int lcm(int a, int b) {
    int i;
    int max = (a > b) ? a : b;

    for (i = max; i <= a * b; i++) {
        if (i % a == 0 && i % b == 0) {
            return i;
        }
    }
    return a * b;
}

int fac(int n) {
    int f = 1;
    while (n > 0) {
        f = f * n;
        n--;
    }
    return f;
}



📌 Step 2 — Compile C to DLL

Open CMD in same folder:

cd "D:\SIRg 100 day\Day_30(Call_fun by python)"
gcc -shared -o customlib.dll customlib.c


➡ customlib.dll will be generated.

📌 Step 3 — Copy DLL Path

Right click customlib.dll

Select Copy as Path

Use it in Python like:

r"D:\SIRg 100 day\Day_30(Call_fun by python)\customlib.dll"

📌 Step 4 — Call C functions from Python
from ctypes import *

lib = CDLL(r"YOUR_DLL_PATH_HERE")

lib.lcm.argtypes = [c_int, c_int]
lib.lcm.restype  = c_int

lib.fac.argtypes = [c_int]
lib.fac.restype  = c_int

print(lib.lcm(4, 6))   # 12
print(lib.fac(5))      # 120

🚀 Output
12
120

🔥 Why This Is Important?

Use C speed inside Python

No rewriting logic — reuse existing C code

Same method used in CPython, NumPy, TensorFlow

Foundation for hybrid performance apps