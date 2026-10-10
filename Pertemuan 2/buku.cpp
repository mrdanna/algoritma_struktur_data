#include <iostream>
#include <conio.h>

using namespace std;

struct buku{
    char judul[15];
    int tahun_terbit;
    int harga;
};

int main()
{
    buku book;
    cout<<"Judul buku    : "; cin>>book.judul;
    cout<<"Tahun terbit  : "; cin>>book.tahun_terbit;
    cout<<"Harga         : "; cin>>book.harga;

    cout<<"\nJudul buku \t: "<<book.judul;
    cout<<"\nTahun terbit \t: "<<book.tahun_terbit;
    cout<<"\nHarga \t\t: "<<book.harga;
    getch();
}