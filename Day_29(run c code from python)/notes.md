<div align="center">

# 🔥 Run C Program Using Python  
### 🚀 Passing Command-Line Arguments & Executing C from Python

![Language](https://img.shields.io/badge/language-C%20%2B%20Python-blue)
![Platform](https://img.shields.io/badge/platform-Windows-green)
![Method](https://img.shields.io/badge/Method-subprocess-yellow)
![Status](https://img.shields.io/badge/Project-Completed-success)

</div>

---

## 📌 Overview

This project demonstrates **how to compile and execute a C program using Python**,  
and **pass input values as command-line arguments**.  
Perfect for students learning **system programming**, **inter-language execution**, or **automation scripts**.

---

## 📁 Project Structure

📦 Run-C-From-Python
├── basic.c # C program to read arguments
├── basic.py # Python program to execute compiled C code
└── README.md



---

## 🧩 Step 1 — C Program (`basic.c`)

```c
#include <stdio.h>

int main(int argc, char* argv[]) {
    printf("Argument Count: %d", argc);
    for(int i = 0; i < argc; i++)
        printf("\n%d. %s", i, argv[i]);
    printf("\n");
    return 0;
}
📝 This prints all command-line arguments passed from Python.

🧩 Step 2 — Compile C File
gcc basic.c -o basic.exe


🔹 This generates basic.exe → which Python will run
🔹 Without compiling, .c file cannot be executed ❗

🧩 Step 3 — Run Using Python (basic.py)
import subprocess

print("Enter three numbers")
a, b, c = input(), input(), input()

subprocess.run(['basic.exe', a, b, c])

🖥 Sample Output
Enter three numbers
10
20
30

Argument Count: 4
0. basic.exe
1. 10
2. 20
3. 30

💡 Key Learnings
Topic	Understanding
.c cannot run directly	Must be compiled first ✔
Command-line arguments	Access via argc & argv[]
Python → C Execution	subprocess.run() is the bridge
Multi-language power	We can integrate systems together 🔥
🚀 Future Scope

🔸 Return values from C to Python
🔸 Perform Sum / Max / Avg using C logic
🔸 GUI → C Execution → Python Output
🔸 Multi-language (C, C++, Rust) execution tests

<div align="center">
⭐ If you like this project, give it a Star on GitHub!

More upcoming experiments: Python ↔ C ↔ C++ ↔ Rust Integration

Made with ❤️ by Vipul

</div> ```