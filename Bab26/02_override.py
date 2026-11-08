class Pelajar:
    def papar(self):
        print("Pelajar biasa")

class PelajarBiasiswa(Pelajar):
    def papar(self):
        print("Pelajar biasiswa")

p1 = Pelajar()
p2 = PelajarBiasiswa()

p1.papar()
p2.papar()
