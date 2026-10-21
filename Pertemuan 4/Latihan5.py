A = [10, 20, 30]
B = [40, 50]
target = 30

gabung = A + B
ditemukan = -1
for i in range(len(gabung)):
    if gabung[i] == target:
        ditemukan = i
        break

print("Gabungan :", gabung)
if ditemukan != -1:
    print(f"{target} ditemukan di indeks {ditemukan}")
else:
    print(f"{target} tidak ditemukan")