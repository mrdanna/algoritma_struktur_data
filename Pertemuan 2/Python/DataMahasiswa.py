from dataclasses import dataclass

@dataclass
class Mahasiswa:
    nim: str
    nama: str
    ipk: float


# Inisialisasi array struct
data = [
    Mahasiswa("2301", "Andi", 3.75),
    Mahasiswa("2302", "Budi", 3.50),
    Mahasiswa("2303", "Citra", 3.90),
]


# 1. Menampilkan semua data
def tampilkan_semua(data):
    print(f"{'NIM':<10}{'Nama':<15}{'IPK':<5}")
    print("-" * 30)
    for m in data:
        print(f"{m.nim:<10}{m.nama:<15}{m.ipk:<5.2f}")


# 2. Menambah data
def tambah_mahasiswa(data, mahasiswa):
    data.append(mahasiswa)


# 3. Mencari berdasarkan NIM
def cari_by_nim(data, nim):
    for i, m in enumerate(data):
        if m.nim == nim:
            return i, m
    return -1, None


# 4. Update IPK
def update_ipk(data, nim, ipk_baru):
    idx, m = cari_by_nim(data, nim)
    if idx != -1:
        data[idx].ipk = ipk_baru
        return True
    return False


# 5. Hapus data
def hapus_by_nim(data, nim):
    idx, m = cari_by_nim(data, nim)
    if idx != -1:
        data.pop(idx)
        return True
    return False


# 6. Menghitung rata-rata IPK
def rata_rata_ipk(data):
    if not data:
        return 0
    return sum(m.ipk for m in data) / len(data)


# 7. Mengurutkan berdasarkan IPK
def urutkan_by_ipk(data, descending=True):
    data.sort(key=lambda m: m.ipk, reverse=descending)


# 8. Binary search berdasarkan NIM, data harus terurut berdasarkan NIM
def binary_search_nim(data, nim):
    data_terurut = sorted(data, key=lambda m: m.nim)
    low = 0
    high = len(data_terurut) - 1

    while low <= high:
        mid = (low + high) // 2
        if data_terurut[mid].nim == nim:
            return data_terurut[mid]
        elif data_terurut[mid].nim < nim:
            low = mid + 1
        else:
            high = mid - 1

    return None


# Demo penggunaan
tampilkan_semua(data)

tambah_mahasiswa(data, Mahasiswa("2304", "Dewi", 3.85))
print("\nSetelah tambah data:")
tampilkan_semua(data)

print("\nCari NIM 2302:")
idx, mhs = cari_by_nim(data, "2302")
print(mhs)

update_ipk(data, "2302", 3.60)
print("\nSetelah update IPK Budi:")
tampilkan_semua(data)

print("\nRata-rata IPK:", round(rata_rata_ipk(data), 2))

urutkan_by_ipk(data, descending=True)
print("\nSetelah diurutkan berdasarkan IPK:")
tampilkan_semua(data)

hasil = binary_search_nim(data, "2303")
print("\nHasil binary search NIM 2303:", hasil)

hapus_by_nim(data, "2301")
print("\nSetelah hapus NIM 2301:")
tampilkan_semua(data)