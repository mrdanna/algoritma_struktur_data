# Program: Sistem Nilai Mahasiswa (Array 1 Dimensi)

def grade(n):
    if n >= 85: return 'A'
    elif n >= 75: return 'B'
    elif n >= 65: return 'C'
    elif n >= 55: return 'D'
    else: return 'E'


# ===== 1. INPUT DATA =====
jumlah = int(input("Jumlah mahasiswa: "))

nama  = []   # array 1D nama
nilai = []   # array 1D nilai

for i in range(jumlah):
    n = input(f"Nama mahasiswa {i+1}: ")
    v = int(input(f"Nilai {n}: "))
    nama.append(n)
    nilai.append(v)

# ===== 2. TABEL NILAI =====
print("\n=== TABEL NILAI ===")
print("No  Nama    Nilai  Grade")
for i in range(jumlah):
    print(f"{i+1:<4}{nama[i]:<8}{nilai[i]:<7}{grade(nilai[i])}")

# ===== 3. STATISTIK =====
rata = sum(nilai) / jumlah

imax = nilai.index(max(nilai))   # indeks nilai tertinggi
imin = nilai.index(min(nilai))   # indeks nilai terendah

print("\n=== STATISTIK ===")
print(f"Rata-rata kelas    : {rata:.2f}")
print(f"Nilai tertinggi    : {nilai[imax]} ({nama[imax]})")
print(f"Nilai terendah     : {nilai[imin]} ({nama[imin]})")

# ===== 4. JUMLAH PER GRADE =====
counter = [0, 0, 0, 0, 0]   # indeks 0=A, 1=B, 2=C, 3=D, 4=E
for v in nilai:
    g = grade(v)
    counter['ABCDE'.index(g)] += 1

print("\nJumlah per grade:")
print(f"  A: {counter[0]}")
print(f"  B: {counter[1]}")
print(f"  C: {counter[2]}")
print(f"  D: {counter[3]}")
print(f"  E: {counter[4]}")

# ===== 5. DI ATAS RATA-RATA =====
print("\nMahasiswa di atas rata-rata:")
for i in range(jumlah):
    if nilai[i] > rata:
        print(f"  - {nama[i]} ({nilai[i]})")