class Pelajar:
    def __init__(self, nama, markah):
        self.nama = nama
        self.markah = markah

    def papar(self):
        print(f"{self.nama} - {self.markah}")


class SistemAnalisis:
    def __init__(self):
        self.senarai = []

    def tambah(self, pelajar):
        self.senarai.append(pelajar)

    def laporan(self):
        for pelajar in self.senarai:
            pelajar.papar()


sistem = SistemAnalisis()
sistem.tambah(Pelajar("Aiman", 85.5))
sistem.tambah(Pelajar("Siti", 90.0))
sistem.laporan()
