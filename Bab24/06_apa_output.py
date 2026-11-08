class Pelajar:
    def __init__(self, nama):
        self.nama = nama

p1 = Pelajar("Aiman")
p2 = p1

p1.nama = "Siti"

print(p1.nama)
print(p2.nama)
