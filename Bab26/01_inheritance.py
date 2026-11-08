class Pelajar:
    def __init__(self, nama, markah):
        self.nama = nama
        self.markah = markah

class PelajarBiasiswa(Pelajar):
    def __init__(self, nama, markah, penaja):
        super().__init__(nama, markah)
        self.penaja = penaja

p1 = PelajarBiasiswa("Aiman", 85.5, "Yayasan Pendidikan")

print(p1.nama)
print(p1.markah)
print(p1.penaja)
