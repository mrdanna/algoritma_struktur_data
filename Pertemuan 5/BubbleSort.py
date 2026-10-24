def bubble_sort(arr):
    """
    Mengurutkan array menggunakan algoritma Bubble Sort.
    Parameter: arr (list) - array yang akan diurutkan (ascending)
    Return: list - array yang sudah terurut (in-place)
    """
    n = len(arr)
    
    for i in range(n):
        swapped = False
        
        # Loop inner: bandingkan pasangan bersebelahan
        # n-i-1 karena elemen terakhir sudah terurut
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Tukar posisi
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # Optimasi: jika tidak ada pertukaran, array sudah terurut
        if not swapped:
            break
    
    return arr


# Contoh penggunaan
data = [64, 34, 25, 12, 22, 11, 90]
print("Sebelum:", data)
bubble_sort(data)
print("Sesudah:", data)