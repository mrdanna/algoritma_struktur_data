nilai = [80, 75, 90, 85, 70]

print(nilai[1:3])    # [75, 90]     (indeks 1 sampai 2)
print(nilai[:3])     # [80, 75, 90] (3 elemen pertama)
print(nilai[2:])     # [90, 85, 70] (dari indeks 2 sampai akhir)
print(nilai[::2])    # [80, 90, 70] (setiap 2 langkah)
print(nilai[::-1])   # [70, 85, 90, 75, 80] (terbalik)