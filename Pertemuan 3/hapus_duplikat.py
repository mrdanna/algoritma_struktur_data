# hapus_duplikat.py

arr = [1, 2, 2, 3, 4, 4, 5, 1, 6]
unik = []

for x in arr:
    if x not in unik:
        unik.append(x)

print("Array asli :", arr)
print("Tanpa duplikat:", unik)