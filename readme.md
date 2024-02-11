# Automasi Setup Server Script

## Deskripsi
Script ini ditulis dalam Bahasa Bash dan bertujuan untuk mengotomatisasi pengaturan server dengan lingkungan yang diminta, serta membuat dan mengelola repository di GitHub.

## Langkah-langkah Otomatisasi
1. **Penyetelan Timezone**: Penyetelan timezone dilakukan ke Asia/Jakarta.
2. **Pembaruan Sistem**: Melakukan update & upgrade sistem operasi.
3. **Instalasi Perangkat Lunak**: Menginstal Git, Curl, ZIP, Python3, Python3-pip, dan Docker.
4. **Manajemen Repository**: Script juga melakukan inisialisasi repository lokal, menambahkan perubahan, membuat commit, menambahkan remote repository GitHub, dan melakukan push ke repository GitHub yang telah dibuat.

## Konfigurasi Pengguna
Sebelum menjalankan script, pastikan sudah memasukkan nilai `USERNAME`, `EMAIL`, dan `REPO_NAME` sesuai dengan informasi GitHub Anda.

## Kunci SSH
Pastikan juga untuk memiliki kunci SSH yang dikonfigurasi di akun GitHub Anda. Hal ini diperlukan untuk memungkinkan push ke repository GitHub tanpa diminta password setiap kali.

## Izin Eksekusi
Sebelum menjalankan script, berikan izin eksekusi pada file dengan menggunakan perintah `chmod +x setupbash.sh`.

## Menjalankan Script
Script dapat dijalankan dengan hak akses superuser atau menggunakan perintah `sudo`. Misalnya, `sudo ./setupbash.sh`. Pastikan Anda berada di direktori yang tepat di mana file skrip ini berada saat menjalankan perintah tersebut.

## Pesan Status
Setelah dijalankan, script ini akan menampilkan pesan status untuk memberi tahu pengguna tentang progresnya.

---
Dibuat oleh Fathurrahman Hernanda Khasan - 11 Februari 2024
