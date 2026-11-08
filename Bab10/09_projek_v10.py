kursus_list = ["Python", "SQL", "Python", "HTML", "SQL", "CSS"]
kursus_unik = set(kursus_list)

print("Senarai asal:", kursus_list)
print("Bilangan asal:", len(kursus_list))
print("Kursus unik:", sorted(kursus_unik))
print("Bilangan unik:", len(kursus_unik))

wajib = {"Python", "SQL"}
print("Kursus wajib:", sorted(wajib))
print("Semua wajib ada:", wajib.issubset(kursus_unik))
