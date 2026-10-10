nilai = [80, 75, 90, 85, 70]

# Cara 1: menggunakan indeks
for i in range(len(nilai)):
    print(f"nilai[{i}] = {nilai[i]}")

# Cara 2: langsung iterasi elemen
for n in nilai:
    print(n)

# Cara 3: indeks + elemen
for i, n in enumerate(nilai):
    print(f"nilai[{i}] = {n}")