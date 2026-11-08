from _sistem import Pelajar, SistemAnalisis

sistem = SistemAnalisis()
sistem.tambah(Pelajar("Aiman Hakim", "Diploma Sains Komputer", 3, 85.5))
sistem.tambah(Pelajar("Siti Aminah", "Diploma Teknologi Maklumat", 3, 90.0))

print(sistem.cari("Aiman Hakim"))
print("Kemas kini:", sistem.kemas_kini("Aiman Hakim", 88.0))
print("Padam:", sistem.padam("Siti Aminah"))
print("Bilangan:", len(sistem.senarai))
