from dataclasses import dataclass

@dataclass
class Pelajar:
    nama: str
    kursus: str
    markah: float

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

p1 = Pelajar("Aiman Hakim", "Diploma Sains Komputer", 85.5)
print(p1)
print("Gred:", p1.gred())
