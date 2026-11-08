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


class SistemAnalisis:
    def __init__(self):
        self.senarai = []

    def tambah(self, pelajar):
        self.senarai.append(pelajar)

    def laporan(self):
        print("=== LAPORAN PELAJAR ===")
        for pelajar in self.senarai:
            pelajar.papar()

    def purata(self):
        if not self.senarai:
            return 0
        jumlah = sum(p.markah for p in self.senarai)
        return jumlah / len(self.senarai)

    def bilangan(self):
        return len(self.senarai)


sistem = SistemAnalisis()
sistem.tambah(Pelajar("Aiman Hakim", 85.5))
sistem.tambah(Pelajar("Siti Aminah", 90.0))
sistem.tambah(Pelajar("Raj Kumar", 78.5))

sistem.laporan()
print("Bilangan pelajar:", sistem.bilangan())
print("Purata kelas:", sistem.purata())
