def insertion_sort(arr):
    """
    Mengurutkan array menggunakan algoritma Insertion Sort.
    Parameter: arr (list) - array yang akan diurutkan (ascending)
    Return: list - array yang sudah terurut (in-place)
    """
    n = len(arr)
    
    for i in range(1, n):
        key = arr[i]          # Elemen yang akan disisipkan
        j = i - 1
        
        # Geser elemen yang lebih besar dari key ke kanan
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Sisipkan key ke posisi yang tepat
        arr[j + 1] = key
    
    return arr


# Contoh penggunaan
data = [12, 11, 13, 5, 6]
print("Sebelum:", data)
insertion_sort(data)
print("Sesudah:", data)