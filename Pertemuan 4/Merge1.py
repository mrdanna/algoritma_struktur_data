def merge_sederhana(arr1, arr2):
    """Menggabungkan dua array tanpa memperhatikan urutan."""
    hasil = []
    for nilai in arr1:
        hasil.append(nilai)
    for nilai in arr2:
        hasil.append(nilai)
    return hasil


# --- Program Utama ---
A = [1, 4, 7]
B = [2, 3, 9]

C = merge_sederhana(B, A)
print("Array A    :", A)
print("Array B    :", B)
print("Hasil merge:", C)