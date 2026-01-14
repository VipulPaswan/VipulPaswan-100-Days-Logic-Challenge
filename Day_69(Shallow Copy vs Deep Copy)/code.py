import copy

original = [[1, 2], [3, 4]]

shallow = copy.copy(original)
deep = copy.deepcopy(original)

shallow[0].append(99)

print("Original:", original)
print("Shallow :", shallow)
print("Deep    :", deep)

# ---------Output-----------
Original: [[1, 2, 99], [3, 4]]
Shallow : [[1, 2, 99], [3, 4]]
Deep    : [[1, 2], [3, 4]]



