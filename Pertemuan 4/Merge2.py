def merge_terurut(A, B):
    """Menggabungkan dua array terurut menaik menjadi satu array terurut."""
    hasil = []
    i = 0
    j = 0

    # Bandingkan elemen dari kedua array
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            hasil.append(A[i])
            i += 1
        else:
            hasil.append(B[j])
            j += 1

    # Salin sisa elemen A (jika masih ada)
    while i < len(A):
        hasil.append(A[i])
        i += 1

    # Salin sisa elemen B (jika masih ada)
    while j < len(B):
        hasil.append(B[j])
        j += 1

    return hasil


# --- Program Utama ---
A = [1, 4, 7]
B = [2, 3, 9, 10]

C = merge_terurut(A, B)
print("Array A    :", A)
print("Array B    :", B)
print("Hasil merge:", C)