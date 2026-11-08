class Pelajar:
    def __init__(self, nama, kursus, markah):
        self.nama = nama
        self.kursus = kursus
        self.markah = markah

    def gred(self):
        if self.markah >= 80:
            return "A"
        elif self.markah >= 70:
            return "B"
        elif self.markah >= 60:
            return "C"
        elif self.markah >= 50:
            return "D"
        elif self.markah >= 40:
            return "E"
        else:
            return "F"

    def papar(self):
        print(f"Nama   : {self.nama}")
        print(f"Kursus : {self.kursus}")
        print(f"Markah : {self.markah}")
        print(f"Gred   : {self.gred()}")

p1 = Pelajar("Aiman Hakim", "Diploma Sains Komputer", 85.5)
p2 = Pelajar("Siti Aminah", "Diploma Teknologi Maklumat", 90.0)

p1.papar()
print("---")
p2.papar()
