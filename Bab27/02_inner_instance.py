class Pelajar:
    class Alamat:
        def __init__(self, bandar):
            self.bandar = bandar

    def __init__(self, nama, bandar):
        self.nama = nama
        self.alamat = self.Alamat(bandar)

p1 = Pelajar("Aiman", "Shah Alam")

print(p1.nama)
print(p1.alamat.bandar)
