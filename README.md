# Sistem Manajemen Kontak

Program Python sederhana untuk mengelola kontak menggunakan konsep pemrograman modular dan pemrograman berorientasi objek (OOP).

## Fitur
- Menambahkan kontak baru dengan nama, nomor telepon, dan email.
- Melihat semua kontak dalam format tabel.
- Menghapus kontak berdasarkan nomor urut.
- Mencari kontak berdasarkan nama.

## Struktur Program
Program ini dibagi menjadi empat modul:
1. **data.py**: Mendefinisikan kelas `Contact` untuk menyimpan informasi kontak.
2. **view.py**: Menangani tampilan pesan dan kontak dalam format yang mudah dibaca.
3. **process.py**: Mengelola logika inti untuk menambah, menghapus, dan mencari kontak.
4. **main.py**: Berisi menu utama dan mengintegrasikan semua modul.

## Validasi Input
- **Nomor telepon**: Harus hanya berisi angka.
- **Email**: Harus mengikuti format standar (contoh: `nama@example.com`).

## Cara Menjalankan
1. Simpan semua file (`data.py`, `view.py`, `process.py`, `main.py`) dalam direktori yang sama.
2. Jalankan program dengan perintah berikut:
   ```bash
   python main.py
   ```
3. Ikuti menu yang ditampilkan di layar untuk menggunakan program.

## Contoh Output
```
Sistem Manajemen Kontak
1. Tambah Kontak
2. Lihat Kontak
3. Hapus Kontak
4. Cari Kontak
5. Keluar
Pilih opsi: 
```

## Persyaratan
- Python 3.x

## Penulis
Fathan Atallah Rasya Nugraha
