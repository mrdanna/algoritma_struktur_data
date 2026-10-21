def sequential_search(arr, target):
    """
    Mencari target dalam array secara berurutan.
    Mengembalikan indeks jika ditemukan, atau -1 jika tidak.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i          # ditemukan
    return -1                 # tidak ditemukan


# --- Program Utama ---
data = [12, 45, 7, 89, 23, 56, 10,23]
cari = 23

hasil = sequential_search(data, cari)

if hasil != -1:
    print(f"Nilai {cari} ditemukan pada indeks {hasil}")
else:
    print(f"Nilai {cari} tidak ditemukan")