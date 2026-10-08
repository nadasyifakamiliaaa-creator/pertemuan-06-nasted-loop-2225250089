n = int(input("n: "))
for i in range(1, n + 1):       # loop luar, menentukan jumlah baris
    for j in range(i):           # loop dalam, jumlah simbol per baris
        print("*", end=" ")      # cetak simbol bintang tanpa pindah baris
    print()                      # pindah ke baris baru setelah loop dalam selesai
