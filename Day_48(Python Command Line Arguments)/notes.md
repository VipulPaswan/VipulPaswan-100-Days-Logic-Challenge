# Day 48 — Python Command Line Arguments

Today I learned how to take input from the command line in Python using the `sys` module.  
Command line arguments allow programs to accept values while running from the terminal.

---

## 🧠 What are Command Line Arguments?

Command line arguments are values passed to a program **when it is executed**, not while it is running.

Example:
```bash
python average.py 10 20 30
Here:

average.py → Script name

10 20 30 → Arguments

📌 sys.argv Explained
sys.argv is a list

sys.argv[0] → Script name

sys.argv[1:] → Actual arguments

All arguments are received as strings.

🧩 Program Explanation
✔ Checks if arguments are provided
✔ Converts arguments to integers
✔ Calculates average
✔ Handles missing input safely
🧩 Code Used (average.py)
python
Copy code
import sys

def average():
    if len(sys.argv) <= 1:
        print("Please pass numbers as command-line arguments")
        return

    l = [int(e) for e in sys.argv[1:]]
    print(sum(l) / len(l))

average()
▶ How to Run the Program
bash
Copy code
python average.py 10 20 30 40
Output:
Copy code
25.0
🎯 Why This Matters?
Command line arguments help:

Write reusable scripts

Automate tasks

Avoid interactive input

Build system-level tools

This is essential knowledge for scripting and backend work.

🏁 Summary
Day 48 strengthened my understanding of how Python programs interact with the operating system.
Command line arguments make scripts powerful, flexible, and automation-ready.