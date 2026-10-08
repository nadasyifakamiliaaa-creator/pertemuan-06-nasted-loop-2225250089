for i in range(1, 5):           # loop luar (baris 1..4)
    total_baris = 0             # inisialisasi total per baris
    for j in range(1, 4):       # loop dalam (kolom 1..3)
        total_baris += i * j    # akumulasi hasil perkalian i * j
    print(f"Jumlah baris {i} = {total_baris}")
