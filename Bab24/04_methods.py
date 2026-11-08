class Pelajar:
    def __init__(self, nama, markah):
        self.nama = nama
        self.markah = markah

    def lulus(self):
        return self.markah >= 60

    def papar(self):
        print(f"{self.nama}: {self.markah}")

p1 = Pelajar("Aiman", 85.5)
p1.papar()
print("Lulus:", p1.lulus())
