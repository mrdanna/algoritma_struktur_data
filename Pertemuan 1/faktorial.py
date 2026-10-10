def Faktorial(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * Faktorial(n - 1)


# Contoh penggunaan program
hasil = Faktorial(100)
print(f"Hasil dari 100! adalah {hasil}")