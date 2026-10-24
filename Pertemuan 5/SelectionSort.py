def selection_sort(arr):
    """
    Mengurutkan array menggunakan algoritma Selection Sort.
    Parameter: arr (list) - array yang akan diurutkan (ascending)
    Return: list - array yang sudah terurut (in-place)
    """
    n = len(arr)
    
    for i in range(n - 1):
        # Cari indeks elemen terkecil di bagian belum terurut
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Tukar elemen terkecil dengan elemen di posisi i
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr


# Contoh penggunaan
data = [64, 25, 12, 22, 11]
print("Sebelum:", data)
selection_sort(data)
print("Sesudah:", data)