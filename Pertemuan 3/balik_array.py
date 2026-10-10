# balik_array.py

arr = [10, 20, 30, 40, 50]
print("Sebelum:", arr)

# Cara 1: slicing
terbalik = arr[::-1]

# Cara 2: dua pointer (in-place)
def balik(arr):
    kiri, kanan = 0, len(arr) - 1
    while kiri < kanan:
        arr[kiri], arr[kanan] = arr[kanan], arr[kiri]
        kiri += 1
        kanan -= 1

balik(arr)
print("Sesudah (in-place):", arr)
print("Sesudah (slicing) :", terbalik)