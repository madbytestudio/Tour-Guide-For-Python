def jumlah(*angka):
    total = 0
    for n in angka:
        total += n
    return total

print(jumlah(1, 2, 3))
print(jumlah(10, 20))
print(jumlah())
