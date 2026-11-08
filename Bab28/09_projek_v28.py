import csv

pelajar = [
    {"nama": "Aiman Hakim", "kursus": "Diploma Sains Komputer", "markah": 85.5},
    {"nama": "Siti Aminah", "kursus": "Diploma Teknologi Maklumat", "markah": 90.0},
    {"nama": "Raj Kumar", "kursus": "Diploma Multimedia", "markah": 78.5},
]

with open("laporan_pelajar.csv", "w", newline="", encoding="utf-8") as fail:
    medan = ["nama", "kursus", "markah"]
    penulis = csv.DictWriter(fail, fieldnames=medan)
    penulis.writeheader()
    penulis.writerows(pelajar)

with open("laporan_pelajar.csv", "r", newline="", encoding="utf-8") as fail:
    pembaca = csv.DictReader(fail)
    for rekod in pembaca:
        print(rekod["nama"], "-", rekod["kursus"], "-", rekod["markah"])
