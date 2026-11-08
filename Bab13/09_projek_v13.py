nama = "Aiman Hakim"
markah = 85.5

if markah >= 80:
    gred = "A"
elif markah >= 70:
    gred = "B"
elif markah >= 60:
    gred = "C"
elif markah >= 50:
    gred = "D"
elif markah >= 40:
    gred = "E"
else:
    gred = "F"

status = "Lulus" if markah >= 60 else "Gagal"

print("Nama:", nama)
print("Markah:", markah)
print("Gred:", gred)
print("Status:", status)
