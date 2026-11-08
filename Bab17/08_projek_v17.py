def kira_purata(jumlah, bilangan):
    return jumlah / bilangan

def tentukan_gred(markah):
    if markah >= 80:
        return "A"
    elif markah >= 70:
        return "B"
    elif markah >= 60:
        return "C"
    elif markah >= 50:
        return "D"
    elif markah >= 40:
        return "E"
    else:
        return "F"

nama = "Aiman Hakim"
markah_1 = 80
markah_2 = 85
markah_3 = 90

jumlah = markah_1 + markah_2 + markah_3
purata = kira_purata(jumlah, 3)
gred = tentukan_gred(purata)

print("Nama:", nama)
print("Jumlah:", jumlah)
print("Purata:", purata)
print("Gred:", gred)
