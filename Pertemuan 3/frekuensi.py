# frekuensi.py

arr = [1, 2, 3, 2, 1, 2, 4, 1, 2, 3]
frekuensi = {}

for x in arr:
    if x in frekuensi:
        frekuensi[x] += 1
    else:
        frekuensi[x] = 1

print("Frekuensi setiap nilai:")
for nilai, jumlah in frekuensi.items():
    print(f"  {nilai} muncul {jumlah} kali")