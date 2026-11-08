class Pelajar:
    def __init__(self, nama):
        self.nama = nama

    def __str__(self):
        return f"Pelajar: {self.nama}"

p = Pelajar("Aiman")

print(p)
print(str(p))
