pelajar = ("Aiman", 20, "Diploma Sains Komputer")

nama, umur, kursus = pelajar

print(nama)
print(umur)
print(kursus)

# Unpacking dengan bintang.
nama, *lain = pelajar
print(nama)
print(lain)
