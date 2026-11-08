def kira_purata(*markah):
    return sum(markah) / len(markah)

def papar_profil(**maklumat):
    for key, value in maklumat.items():
        print(f"{key}: {value}")

papar_profil(nama="Aiman Hakim", kursus="Diploma Sains Komputer", semester=3)
purata = kira_purata(80, 85, 90)
print("Purata:", purata)
