from ctypes import *

lib = CDLL(r"customlib.dll ka file path copy and paste")

print(lib.lcm(4,6))  # Output → 12
print(lib.fac(5))    # Output → 120




