A = [1, 10]
B = [2, 3, 4, 5, 20]

hasil = []
i = j = 0

while i < len(A) and j < len(B):
    if A[i] <= B[j]:
        hasil.append(A[i]); i += 1
    else:
        hasil.append(B[j]); j += 1

while i < len(A):
    hasil.append(A[i]); i += 1
while j < len(B):
    hasil.append(B[j]); j += 1

print(hasil)   # [1, 2, 3, 4, 5, 10, 20]