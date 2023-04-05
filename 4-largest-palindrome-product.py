digits = 3
pal = 0
for i in range(10**digits - 1, 99, -1):
    for j in range(10**digits - 1, i-1, -1):
        prod = i*j
        if str(prod) == str(prod)[::-1] and prod > pal:
            pal = prod
print(pal)
