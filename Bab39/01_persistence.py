from _app import Pelajar, simpan, muat

pelajar = [
    Pelajar("Aiman Hakim", "Diploma Sains Komputer", 3, 85.5, 90),
    Pelajar("Siti Aminah", "Diploma Teknologi Maklumat", 3, 90.0, 95),
]

simpan(pelajar, "data_pelajar.json")

dimuat = muat("data_pelajar.json")

for p in dimuat:
    print(p)
