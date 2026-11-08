class Pelajar:
    def __init__(self, nama, markah):
        self.nama = nama
        self.markah = markah

p1 = Pelajar("Aiman", 85.5)
print(p1.nama, p1.markah)

p1.markah = 90.0
p1.semester = 3
print(p1.nama, p1.markah, p1.semester)

del p1.semester
print(hasattr(p1, "semester"))
