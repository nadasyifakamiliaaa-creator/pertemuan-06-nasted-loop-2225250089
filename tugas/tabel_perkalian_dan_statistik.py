print("Tabel Perkalian dan Statistik")

# Validasi input n (harus positif)
n = int(input("n: "))
while n <= 0:
    print("n harus lebih dari 0!")
    n = int(input("n: "))

# Inisialisasi total keseluruhan dan counter genap
total_semua = 0
count_genap = 0

# Nested loop untuk tabel perkalian
for i in range(1, n + 1):
    total_baris = 0
    for j in range(1, n + 1):
        hasil = i * j
        print(f"{hasil:3}", end=" ")   # cetak tabel dengan lebar 3
        total_baris += hasil           # akumulasi per baris
        total_semua += hasil           # akumulasi keseluruhan
        if hasil % 2 == 0:             # pencacahan bilangan genap
            count_genap += 1
    print(f" | Jumlah baris {i} = {total_baris}")

# Statistik keseluruhan
print(f"Total keseluruhan = {total_semua}")
print(f"Banyak hasil genap = {count_genap}")
