from _sistem import Pelajar, SistemAnalisis

sistem = SistemAnalisis()
sistem.tambah(Pelajar("Aiman", "DSC", 3, 70))
sistem.tambah(Pelajar("Siti", "DIT", 3, 90))

print(len(sistem.senarai))
print(sistem.purata())
print(sistem.cari("Siti").gred())
