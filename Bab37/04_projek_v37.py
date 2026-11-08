from dataclasses import dataclass

@dataclass
class Pelajar:
    nama: str
    kursus: str
    markah: float

    def __post_init__(self):
        if not 0 <= self.markah <= 100:
            raise ValueError("Markah mesti antara 0 dan 100")

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

class SistemAnalisis:
    def __init__(self):
        self.senarai = []

    def tambah(self, pelajar):
        self.senarai.append(pelajar)

    def laporan(self):
        for p in self.senarai:
            print(f"{p.nama} - {p.kursus} - {p.markah} - {p.gred()}")

sistem = SistemAnalisis()
sistem.tambah(Pelajar("Aiman Hakim", "Diploma Sains Komputer", 85.5))
sistem.tambah(Pelajar("Siti Aminah", "Diploma Teknologi Maklumat", 90.0))

sistem.laporan()
