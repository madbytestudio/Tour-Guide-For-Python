class Pelajar:
    def __init__(self, nama):
        self.nama = nama

    def sapaan(self):
        print("Hello, saya", self.nama)

p1 = Pelajar("Aiman")
p2 = Pelajar("Siti")

p1.sapaan()
p2.sapaan()
