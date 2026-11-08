class Pelajar:
    def __init__(self, nama, markah):
        self.nama = nama
        self.__markah = markah

    def get_markah(self):
        return self.__markah

    def set_markah(self, markah):
        if 0 <= markah <= 100:
            self.__markah = markah
        else:
            print("Markah tidak sah")

p1 = Pelajar("Aiman", 85.5)

print(p1.get_markah())
p1.set_markah(90)
print(p1.get_markah())
p1.set_markah(150)
print(p1.get_markah())
