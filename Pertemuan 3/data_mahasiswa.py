# data_mahasiswa.py

nama = ["Andi", "Budi", "Citra", "Dewi", "Eka"]
nilai = [80, 75, 90, 85, 70]

print("=== DAFTAR NILAI MAHASISWA ===")
for i in range(len(nama)):
    status = "LULUS" if nilai[i] >= 75 else "TIDAK LULUS"
    print(f"{nama[i]:<8} : {nilai[i]:>3}  [{status}]")

rata = sum(nilai) / len(nilai)
print(f"\nRata-rata kelas: {rata:.2f}")