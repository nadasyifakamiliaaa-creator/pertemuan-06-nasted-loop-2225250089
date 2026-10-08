count = 0
for i in range(1, 4):          # loop luar (i = 1..3)
    for j in range(1, 5):      # loop dalam (j = 1..4)
        print(i, j)            # tampilkan pasangan i, j
        count += 1             # tambahkan counter
print(f"Banyak pasangan = {count}")
