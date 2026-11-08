def carian_binari(senarai, sasaran):
    kiri, kanan = 0, len(senarai) - 1

    while kiri <= kanan:
        tengah = (kiri + kanan) // 2
        if senarai[tengah] == sasaran:
            return tengah
        elif senarai[tengah] < sasaran:
            kiri = tengah + 1
        else:
            kanan = tengah - 1

    return -1

nama = ["Aiman", "Mei", "Raj", "Siti", "Zul"]

print(carian_binari(nama, "Siti"))
print(carian_binari(nama, "Ali"))
