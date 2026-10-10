# cari_maks.py

arr = [80, 75, 90, 85, 70]
maks = arr[0]
idx_maks = 0

for i in range(1, len(arr)):
    if arr[i] > maks:
        maks = arr[i]
        idx_maks = i

print(f"Nilai maksimum: {maks} pada indeks {idx_maks}")