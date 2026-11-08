import datetime
import math

nama = "Aiman Hakim"
markah = [85.5, 90.0, 78.5]
purata = sum(markah) / len(markah)
purata_bulat = round(purata, 2)

print("Tarikh laporan:", datetime.date.today().strftime("%d/%m/%Y"))
print("Nama:", nama)
print("Purata:", purata_bulat)
print("Purata ceil:", math.ceil(purata))
print("Purata floor:", math.floor(purata))
