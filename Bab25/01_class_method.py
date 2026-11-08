class Pelajar:
    def __init__(self, nama, markah):
        self.nama = nama
        self.markah = markah

    @classmethod
    def dari_string(cls, teks):
        nama, markah = teks.split(",")
        return cls(nama, float(markah))

p1 = Pelajar.dari_string("Aiman,85.5")
print(p1.nama, p1.markah)
