import subprocess

print("Enter three numbers")
a, b, c = input(), input(), input()

subprocess.run(['basic.exe', a, b, c])




"""
# ---- OUTPUT ----- 

Enter three numbers
10
20
30
Argument Count: 4
0. basic.exe
1. 10
2. 20
3. 30

"""
