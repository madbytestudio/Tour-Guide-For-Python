class Pelajar:
    def __init__(self, nama, kursus="Diploma Sains Komputer"):
        self.nama = nama
        self.kursus = kursus

p1 = Pelajar("Aiman")
p2 = Pelajar("Siti", "Diploma Teknologi Maklumat")

print(p1.nama, p1.kursus)
print(p2.nama, p2.kursus)
