# Pertemuan 06 Nested Loop Python
Algoritma dan Pemrograman | Pertemuan 06 | 12

Nama: Nada Syifa Kamilia
NIM: 2225520089  
Kelas: 3B  

## Tujuan
Menggunakan nested loop untuk membentuk pola, melakukan akumulasi nilai, dan pencacahan kondisi tertentu.

## Cara Menjalankan
```bash
python3 tugas/tabel_perkalian_dan_statistik.py
print("Tabel Perkalian dan Statistik")

# Validasi input n (harus lebih dari 0)
n = int(input("n: "))
while n <= 0:
    print("n harus lebih dari 0!")
    n = int(input("n: "))

# Inisialisasi akumulator dan counter global
total_semua = 0
count_genap = 0

# Nested loop
for i in range(1, n + 1):          # loop luar = baris
    total_baris = 0                # akumulator per baris
    for j in range(1, n + 1):      # loop dalam = kolom
        hasil = i * j
        print(f"{hasil:3}", end=" ")   # cetak tabel dengan lebar 3
        total_baris += hasil           # akumulasi per baris
        total_semua += hasil           # akumulasi keseluruhan
        if hasil % 2 == 0:             # pencacahan hasil genap
            count_genap += 1
    print(f" | Jumlah baris {i} = {total_baris}")

# Statistik keseluruhan
print(f"Total keseluruhan = {total_semua}")
print(f"Banyak hasil genap = {count_genap}")
print("=== Hasil Pengujian Tabel Perkalian ===")

# Input uji coba
n = 3
print(f"Input: n = {n}")

# Inisialisasi
total_semua = 0
count_genap = 0

# Keluaran aktual
for i in range(1, n + 1):
    total_baris = 0
    for j in range(1, n + 1):
        hasil = i * j
        print(f"{hasil:3}", end=" ")
        total_baris += hasil
        total_semua += hasil
        if hasil % 2 == 0:
            count_genap += 1
    print(f" | Jumlah baris {i} = {total_baris}")

print(f"Total keseluruhan = {total_semua}")
print(f"Banyak hasil genap = {count_genap}")

# Keluaran yang diharapkan
expected_total_semua = 36
expected_count_genap = 5

print("\n=== Verifikasi ===")
print(f"Hasil yang diharapkan total = {expected_total_semua}")
print(f"Hasil yang diharapkan genap = {expected_count_genap}")

# Status
if total_semua == expected_total_semua and count_genap == expected_count_genap:
    print("Status: ✅ Sesuai")
else:
    print("Status: ❌ Tidak sesuai")
print("=== Analisis Efisiensi Nested Loop ===")

# Input uji coba
n = int(input("n: "))
while n <= 0:
    print("n harus lebih dari 0!")
    n = int(input("n: "))

# Hitung jumlah iterasi badan loop dalam
iterasi = 0
for i in range(1, n + 1):        # loop luar
    for j in range(1, n + 1):    # loop dalam
        iterasi += 1             # setiap kali badan loop dalam dijalankan

print(f"Jumlah iterasi badan loop dalam = {iterasi}")
print(f"Rumus umum: n × n = {n} × {n} = {iterasi}")
print("=== Refleksi Nested Loop ===")

# Contoh kesalahan: inisialisasi akumulator di tempat yang salah
print("\nContoh Kesalahan:")
try:
    n = 3
    total_baris = 0   # ❌ Salah: diletakkan di luar loop luar
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            total_baris += i * j
        print(f"Jumlah baris {i} = {total_baris}")  # hasil tidak reset per baris
except Exception as e:
    print("Error yang muncul:", e)

# Perbaikan: inisialisasi akumulator di dalam loop luar
print("\nPerbaikan:")
n = 3
for i in range(1, n + 1):
    total_baris = 0   # ✅ Benar: reset setiap baris
    for j in range(1, n + 1):
        total_baris += i * j
    print(f"Jumlah baris {i} = {total_baris}")
