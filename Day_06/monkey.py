import math
import time

# Original function (from built-in module)
result = math.sqrt(16)
print(result)   # Output: 4.0

# Monkey patching: wrap the original function with logging
original_sqrt = math.sqrt   # Backup original

def logged_sqrt(x):
    start = time.time()
    result = original_sqrt(x)
    end = time.time()
    print(f"[LOG] math.sqrt({x}) = {result} (executed in {end - start:.6f}s)")
    return result

# Apply the patch at runtime
math.sqrt = logged_sqrt

# Now every call to math.sqrt() is automatically logged!
print(math.sqrt(25))
print(math.sqrt(49))





