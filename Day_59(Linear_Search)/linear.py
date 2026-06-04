def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


data = [17, 20, 35, 43, 55, 76, 81, 92]
target = 43

print("Index:", linear_search(data, target))

# ---- OUTPUT ----
Index: 3