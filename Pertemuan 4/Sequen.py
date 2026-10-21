def apakah_ada(arr, target):
    """Mengembalikan True jika target ada, False jika tidak."""
    for nilai in arr:
        if nilai == target:
            return True
    return False


# --- Program Utama ---
data = [12, 45, 7, 89, 23, 56, 10]

print(apakah_ada(data, 89))   # True
print(apakah_ada(data, 100))  # False