from _sistem import Pelajar, SistemAnalisis

sistem = SistemAnalisis()

sistem.tambah(Pelajar("Aiman Hakim", "Diploma Sains Komputer", 3, 85.5, 90))
sistem.tambah(Pelajar("Siti Aminah", "Diploma Teknologi Maklumat", 3, 90.0, 95))
sistem.tambah(Pelajar("Raj Kumar", "Diploma Multimedia", 3, 55.0, 70))

sistem.laporan()
print("Purata:", sistem.purata())
print("Ringkasan:", sistem.ringkasan())
print()

print("Carian Raj:", sistem.cari("Raj Kumar"))
print("Kemas kini Raj:", sistem.kemas_kini("Raj Kumar", 65.0))
print("Padam Siti:", sistem.padam("Siti Aminah"))
print()

sistem.laporan()
print("Purata akhir:", sistem.purata())
