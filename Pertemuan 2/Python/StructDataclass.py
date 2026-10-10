from dataclasses import dataclass

@dataclass
class Mahasiswa:
    nim: str
    nama: str
    ipk: float

mhs1 = Mahasiswa("2301", "Andi", 3.75)
print(mhs1.nim)
print(mhs1.nama)
print(mhs1.ipk)