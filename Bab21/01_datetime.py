import datetime

sekarang = datetime.datetime.now()
hari_ini = datetime.date.today()

print("Sekarang:", sekarang)
print("Hari ini:", hari_ini)
print("Tahun:", sekarang.year)
print("Bulan:", sekarang.month)
print("Hari:", sekarang.day)
print("Jam:", sekarang.hour)
print("Minit:", sekarang.minute)
print("Format:", sekarang.strftime("%d/%m/%Y %H:%M"))
