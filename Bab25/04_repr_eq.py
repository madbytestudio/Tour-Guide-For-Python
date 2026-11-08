class Pelajar:
    def __init__(self, nama, markah):
        self.nama = nama
        self.markah = markah

    def __repr__(self):
        return f"Pelajar('{self.nama}', {self.markah})"

    def __eq__(self, other):
        return self.nama == other.nama and self.markah == other.markah

p1 = Pelajar("Aiman", 85.5)
p2 = Pelajar("Aiman", 85.5)

print(repr(p1))
print(p1 == p2)
