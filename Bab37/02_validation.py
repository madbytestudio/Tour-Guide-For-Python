from dataclasses import dataclass

@dataclass
class Pelajar:
    nama: str
    kursus: str
    markah: float

    def __post_init__(self):
        if not 0 <= self.markah <= 100:
            raise ValueError("Markah mesti antara 0 dan 100")

p1 = Pelajar("Aiman Hakim", "Diploma Sains Komputer", 85.5)
print(p1)

try:
    Pelajar("Siti Aminah", "Diploma Teknologi Maklumat", 150)
except ValueError as e:
    print("Ralat:", e)
