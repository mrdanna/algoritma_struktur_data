from collections import namedtuple

Mahasiswa = namedtuple("Mahasiswa", ["nim", "nama", "ipk"])

mhs = Mahasiswa("2302", "Budi", 3.50)
print(mhs.nama)
print(mhs.ipk)