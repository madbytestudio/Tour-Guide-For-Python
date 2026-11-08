class Pelajar:
    def __init__(self, nama, markah):
        self.nama = nama
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
        print(f"{self.nama} - {self.markah} - {self.gred()}")

class PelajarBiasiswa(Pelajar):
    def __init__(self, nama, markah, penaja):
        super().__init__(nama, markah)
        self.penaja = penaja

    def papar(self):
        print(f"{self.nama} - {self.markah} - {self.gred()} - Biasiswa: {self.penaja}")

senarai = [
    Pelajar("Aiman Hakim", 85.5),
    PelajarBiasiswa("Siti Aminah", 90.0, "Yayasan Pendidikan"),
]

for p in senarai:
    p.papar()
