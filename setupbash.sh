#!/bin/bash

# Nama Script: setup_server.sh
# Deskripsi: Script untuk mengotomatisasi pengaturan server dengan lingkungan yang diminta
# Pembuat: Fathurrahman Hernanda Khasan
# Tanggal Pembuatan: 10 Februari 2024

# Fungsi untuk menampilkan pesan dengan format tertentu
log() {
    echo -e "\e[32m[INFO] $1\e[0m"
}

# Fungsi untuk menampilkan pesan error dengan format tertentu
error() {
    echo -e "\e[91m[ERROR] $1\e[0m"
}

# 1. Set Timezone ke Asia/Jakarta
log "Setting Timezone ke Asia/Jakarta"
sudo timedatectl set-timezone Asia/Jakarta

# 2. Update & upgrade sistem
log "Melakukan update & upgrade sistem"
sudo apt update -y && sudo apt upgrade -y

# 3. Install Git, Curl, ZIP, Python3, dan Python3-pip
log "Menginstal Git, Curl, ZIP, Python3, dan Python3-pip"
sudo apt install -y git curl zip python3 python3-pip

# 4. Install Docker
log "Menginstal Docker"
sudo apt install -y docker.io

# 5. Restart Docker Service
log "Restarting Docker Service"
sudo systemctl restart docker

# 6. Buat akun GitHub dan push script otomasi ke repository yang telah dibuat
log "Memulai proses push ke GitHub"
# Tentukan username dan email GitHub Anda
USERNAME="fahernkhan"
EMAIL="fathurrahmanhernanda@gmail.com"

# Konfigurasi git
git config --global user.email "$EMAIL"
git config --global user.name "$USERNAME"

# Inisialisasi repository lokal
git init

# Tambahkan semua perubahan ke repository
git add .

# Buat commit
git commit -m "Initial commit"

# Tambahkan remote repository GitHub Anda
git remote add origin https://github.com/$USERNAME/Setup-server-script.git

# Push ke repository GitHub
git push -u origin master

# Jika ada error dalam proses push, tampilkan pesan kesalahan
if [ $? -ne 0 ]; then
    error "Gagal melakukan push ke GitHub. Pastikan Anda telah membuat repository di GitHub dan mengatur kunci SSH."
else
    log "Berhasil melakukan push ke GitHub."
fi

