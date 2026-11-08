from _app import Pelajar, SistemAnalisis

def uji_tambah():
    sistem = SistemAnalisis()
    sistem.tambah(Pelajar("Aiman", "DSC", 3, 85.5))
    assert len(sistem.senarai) == 1
    print("uji_tambah: lulus")

def uji_cari():
    sistem = SistemAnalisis()
    sistem.tambah(Pelajar("Aiman", "DSC", 3, 85.5))
    assert sistem.cari("aiman") is not None
    assert sistem.cari("Ali") is None
    print("uji_cari: lulus")

def uji_purata():
    sistem = SistemAnalisis()
    sistem.tambah(Pelajar("Aiman", "DSC", 3, 80.0))
    sistem.tambah(Pelajar("Siti", "DIT", 3, 90.0))
    assert sistem.purata() == 85.0
    print("uji_purata: lulus")

def uji_padam():
    sistem = SistemAnalisis()
    sistem.tambah(Pelajar("Aiman", "DSC", 3, 85.5))
    assert sistem.padam("Aiman") is True
    assert len(sistem.senarai) == 0
    print("uji_padam: lulus")
