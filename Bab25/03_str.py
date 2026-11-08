class Pelajar:
    def __init__(self, nama, markah):
        self.nama = nama
        self.markah = markah

    def __str__(self):
        return f"Pelajar({self.nama}, {self.markah})"

p1 = Pelajar("Aiman", 85.5)
print(p1)
