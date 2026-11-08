from dataclasses import dataclass

@dataclass
class Pelajar:
    nama: str
    markah: float

p = Pelajar("Aiman", 85.5)

print(p)
print(p.nama)
