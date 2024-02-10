#!/usr/bin/env python3

import os
import subprocess

# Fungsi untuk menampilkan pesan informasi
def log(message):
    print("\033[32m[INFO] {}\033[0m".format(message))

# Fungsi untuk menampilkan pesan kesalahan
def error(message):
    print("\033[91m[ERROR] {}\033[0m".format(message))

# 1. Set Timezone ke Asia/Jakarta
log("Setting Timezone ke Asia/Jakarta")
subprocess.run(["sudo", "timedatectl", "set-timezone", "Asia/Jakarta"])

# 2. Update & upgrade sistem
log("Melakukan update & upgrade sistem")
subprocess.run(["sudo", "apt", "update", "-y"])
subprocess.run(["sudo", "apt", "upgrade", "-y"])

# 3. Install Git, Curl, ZIP, Python3, dan Python3-pip
log("Menginstal Git, Curl, ZIP, Python3, dan Python3-pip")
subprocess.run(["sudo", "apt", "install", "-y", "git", "curl", "zip", "python3", "python3-pip"])

# 4. Install Docker
log("Menginstal Docker")
subprocess.run(["sudo", "apt", "install", "-y", "docker.io"])

# 5. Restart Docker Service
log("Restarting Docker Service")
subprocess.run(["sudo", "systemctl", "restart", "docker"])

# 6. Buat akun GitHub dan push script otomasi ke repository yang telah dibuat
log("Memulai proses push ke GitHub")

# Tentukan username dan email GitHub Anda
USERNAME = "fahernkhan"
EMAIL = "fathurrahmanhernanda123@gmail.com"

# Konfigurasi git
os.system("git config --global user.email {}".format(EMAIL))
os.system("git config --global user.name {}".format(USERNAME))

# Inisialisasi repository lokal
os.system("git init")

# Tambahkan semua perubahan ke repository
os.system("git add .")

# Buat commit
os.system("git commit -m 'Initial commit'")

# Tambahkan remote repository GitHub Anda
os.system("git remote add origin git@github.com:{}/nama-repository.git".format(USERNAME))

# Push ke repository GitHub
os.system("git push -u origin master")

# Jika ada error dalam proses push, tampilkan pesan kesalahan
if $? != 0:
    error("Gagal melakukan push ke GitHub. Pastikan Anda telah membuat repository di GitHub dan mengatur kunci SSH.")
else:
    log("Berhasil melakukan push ke GitHub.")
