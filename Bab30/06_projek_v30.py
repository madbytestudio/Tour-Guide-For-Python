def kira_purata(markah):
    return sum(markah) / len(markah)

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

def uji_purata():
    assert kira_purata([80, 90]) == 85
    assert kira_purata([100]) == 100
    print("Uji purata: lulus")

def uji_gred():
    assert tentukan_gred(85) == "A"
    assert tentukan_gred(75) == "B"
    assert tentukan_gred(35) == "F"
    print("Uji gred: lulus")

uji_purata()
uji_gred()

print("Semua ujian selesai")
