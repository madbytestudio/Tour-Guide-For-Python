class SenaraiMarkah:
    def __init__(self, markah):
        self.markah = markah

    def __len__(self):
        return len(self.markah)

    def __add__(self, other):
        return SenaraiMarkah(self.markah + other.markah)

a = SenaraiMarkah([80, 90])
b = SenaraiMarkah([85, 95])

print(len(a))
print((a + b).markah)
