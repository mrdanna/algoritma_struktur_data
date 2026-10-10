#include <stdio.h>
#include <conio.h>
#include <string.h> // Tambahkan ini untuk strcspn

//struct pertama
struct alamat {
    char Jalan[40]; int NoRumah;
    char Kota[20];
};
//struct kedua
struct tanggalLahir {
    int Tanggal, Bulan, Tahun;
};
//struct ketiga
struct mhs{
    int Nim;
    char Nama[20];
    struct alamat address;
    struct tanggalLahir tgllahir;
};

mhs mahasiswa,alamat,address,tanggalLahir,tgllahir;

int main() // Ubah main() menjadi int main()
{
    //proses input
    printf("Input Nim ="); scanf("%i",&mahasiswa.Nim);
    
    // Ganti gets() dengan fgets() dan hapus newline
    printf("Input Nama Mahasiswa="); fflush(stdin);
    fgets(mahasiswa.Nama, 20, stdin);
    mahasiswa.Nama[strcspn(mahasiswa.Nama, "\n")] = 0;

    printf("Input Nama Jalan ="); fflush(stdin);
    fgets(alamat.address.Jalan, 40, stdin);
    alamat.address.Jalan[strcspn(alamat.address.Jalan, "\n")] = 0;

    printf("Input Kota ="); fflush(stdin);
    fgets(alamat.address.Kota, 20, stdin);
    alamat.address.Kota[strcspn(alamat.address.Kota, "\n")] = 0;

    printf("Input No. Rumah ="); scanf("%i",&alamat.address.NoRumah);
    printf("Input Tanggal Lahir ="); scanf("%i",&tanggalLahir.tgllahir.Tanggal);
    printf("Input Bulan [1-12] ="); scanf("%i",&tanggalLahir.tgllahir.Bulan);
    printf("Input Tahun Lahir ="); scanf("%i",&tanggalLahir.tgllahir.Tahun);

    //proses output
    printf("===============================================\n");
    printf("Nim Mahasiswa =%i",mahasiswa.Nim);
    printf("\nNama Mahasiswa \t =%s",mahasiswa.Nama);
    printf("\nNama Jalan =%s",alamat.address.Jalan);
    printf("\nKota =%s",alamat.address.Kota);
    printf("\nNo. Rumah \t =%i",alamat.address.NoRumah);
    printf("\nTanggal Lahir \t =%i",tanggalLahir.tgllahir.Tanggal);
    printf("\nBulan [1-12] \t =%i",tanggalLahir.tgllahir.Bulan);
    printf("\nInput Tahun Lahir \t =%i",tanggalLahir.tgllahir.Tahun);
    
    getch(); // Tambahkan getch() di akhir agar layar tidak langsung tertutup
    return 0;
}