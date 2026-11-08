class Pelajar:
    def __init__(self, nama):
        self.nama = nama

    def papar(self):
        print("Pelajar:", self.nama)

class PelajarBiasiswa(Pelajar):
    def __init__(self, nama, penaja):
        super().__init__(nama)
        self.penaja = penaja

    def papar(self):
        print("Pelajar biasiswa:", self.nama, "-", self.penaja)

senarai = [Pelajar("Aiman"), PelajarBiasiswa("Siti", "Yayasan")]

for p in senarai:
    p.papar()
