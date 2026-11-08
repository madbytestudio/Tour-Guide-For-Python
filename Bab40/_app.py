import json
from dataclasses import dataclass

@dataclass
class Pelajar:
    nama: str
    kursus: str
    semester: int
    markah: float
    kehadiran: float = 100.0

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

    def status(self):
        return "Lulus" if self.markah >= 60 else "Gagal"


class SistemAnalisis:
    def __init__(self):
        self.senarai = []

    def tambah(self, pelajar):
        self.senarai.append(pelajar)

    def cari(self, nama):
        for p in self.senarai:
            if p.nama.lower() == nama.lower():
                return p
        return None

    def kemas_kini(self, nama, markah):
        p = self.cari(nama)
        if p is None:
            return False
        p.markah = markah
        return True

    def padam(self, nama):
        p = self.cari(nama)
        if p is None:
            return False
        self.senarai.remove(p)
        return True

    def laporan(self):
        for p in sorted(self.senarai, key=lambda x: x.markah, reverse=True):
            print(f"{p.nama} - {p.kursus} - {p.markah} - {p.gred()} - {p.status()}")

    def purata(self):
        if not self.senarai:
            return 0
        return sum(p.markah for p in self.senarai) / len(self.senarai)

    def ringkasan(self):
        lulus = sum(1 for p in self.senarai if p.status() == "Lulus")
        return len(self.senarai), lulus


def simpan(senarai, laluan):
    with open(laluan, "w", encoding="utf-8") as fail:
        json.dump([p.__dict__ for p in senarai], fail, indent=2, ensure_ascii=False)


def muat(laluan):
    with open(laluan, "r", encoding="utf-8") as fail:
        data = json.load(fail)
    return [Pelajar(**item) for item in data]
