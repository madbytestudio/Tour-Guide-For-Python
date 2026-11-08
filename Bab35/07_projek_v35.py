def carian_binari(data, kunci, sasaran):
    kiri, kanan = 0, len(data) - 1

    while kiri <= kanan:
        tengah = (kiri + kanan) // 2
        nilai = data[tengah][kunci]
        if nilai == sasaran:
            return data[tengah]
        elif nilai < sasaran:
            kiri = tengah + 1
        else:
            kanan = tengah - 1

    return None

pelajar = [
    {"nama": "Siti", "markah": 90.0},
    {"nama": "Aiman", "markah": 85.5},
    {"nama": "Raj", "markah": 78.5},
    {"nama": "Mei", "markah": 88.0},
]

mengikut_nama = sorted(pelajar, key=lambda p: p["nama"])
hasil = carian_binari(mengikut_nama, "nama", "Raj")
print("Carian Raj:", hasil)

peringkat = sorted(pelajar, key=lambda p: p["markah"], reverse=True)
print("Peringkat markah:")
for p in peringkat:
    print(p["nama"], "-", p["markah"])
