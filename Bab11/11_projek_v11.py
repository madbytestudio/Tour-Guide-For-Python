pelajar = [
    {"nama": "Aiman Hakim", "kursus": "Diploma Sains Komputer", "markah": 85.5},
    {"nama": "Siti Aminah", "kursus": "Diploma Teknologi Maklumat", "markah": 90.0},
    {"nama": "Raj Kumar", "kursus": "Diploma Multimedia", "markah": 78.5},
]

print("===================================")
print("SISTEM ANALISIS KEPUTUSAN PELAJAR")
print("===================================")
print("Bilangan pelajar:", len(pelajar))
print()

for rekod in pelajar:
    print("Nama   :", rekod["nama"])
    print("Kursus :", rekod["kursus"])
    print("Markah :", rekod["markah"])
    print("---")
