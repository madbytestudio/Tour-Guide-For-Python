class Pelajar:
    def __init__(self, nama, markah):
        self.nama = nama
        self.markah = markah

    def __str__(self):
        return f"{self.nama} ({self.markah})"


class SenaraiPelajar:
    def __init__(self, pelajar):
        self.pelajar = pelajar

    def __len__(self):
        return len(self.pelajar)

    def __str__(self):
        return f"SenaraiPelajar dengan {len(self)} pelajar"

    @classmethod
    def dari_dict(cls, data):
        return cls([Pelajar(**item) for item in data])


data = [
    {"nama": "Aiman", "markah": 85.5},
    {"nama": "Siti", "markah": 90.0},
]

senarai = SenaraiPelajar.dari_dict(data)

print(senarai)
print("Bilangan:", len(senarai))

for p in senarai.pelajar:
    print(p)
