from _app import Pelajar, SistemAnalisis

sistem = SistemAnalisis()
sistem.tambah(Pelajar("Aiman", "DSC", 3, 80))
sistem.tambah(Pelajar("Siti", "DIT", 3, 90))

print(sistem.purata())
print(sistem.ringkasan())
