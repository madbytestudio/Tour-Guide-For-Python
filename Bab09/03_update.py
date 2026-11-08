kursus = ("Python", "SQL", "HTML")

# Tuple tidak boleh diubah secara langsung.
senarai = list(kursus)
senarai[1] = "MySQL"
kursus = tuple(senarai)

print(kursus)

del kursus
print("Tuple telah dipadam.")
