class Mahasiswa:
    def __init__(self, nim, nama, ipk):
        self.nim = nim
        self.nama = nama
        self.ipk = ipk

    def __str__(self):
        return f"{self.nim} - {self.nama} - {self.ipk}"

mhs = Mahasiswa("2303", "Citra", 3.90)
print(mhs)