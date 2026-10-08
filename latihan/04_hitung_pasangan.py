n = int(input("n: "))
count = 0
for i in range(1, n + 1):          # loop luar
    for j in range(1, n + 1):      # loop dalam
        if i + j <= n:             # syarat pasangan
            count += 1             # tambahkan counter
print(f"Banyak pasangan = {count}")
