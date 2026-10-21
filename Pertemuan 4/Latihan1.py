A = [1, 2, 3]
B = [4, 5, 6]

# Cara 1: operator +
C = A + B
print(C)   # [1, 2, 3, 4, 5, 6]

# Cara 2: manual dengan loop
C = []
for x in A:
    C.append(x)
for x in B:
    C.append(x)
print(C)   # [1, 2, 3, 4, 5, 6]