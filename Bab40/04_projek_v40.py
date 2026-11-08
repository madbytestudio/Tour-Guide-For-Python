import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from _app import Pelajar, SistemAnalisis, simpan, muat
from _tests import uji_tambah, uji_cari, uji_purata, uji_padam

sistem = SistemAnalisis()
sistem.tambah(Pelajar("Aiman Hakim", "Diploma Sains Komputer", 3, 85.5, 90))
sistem.tambah(Pelajar("Siti Aminah", "Diploma Teknologi Maklumat", 3, 90.0, 95))
sistem.tambah(Pelajar("Raj Kumar", "Diploma Multimedia", 3, 78.5, 80))

simpan(sistem.senarai, "data_final.json")
dimuat = muat("data_final.json")

print("=== LAPORAN AKHIR ===")
for p in sorted(dimuat, key=lambda x: x.markah, reverse=True):
    print(f"{p.nama} - {p.markah} - {p.gred()} - {p.status()}")

print("Purata:", sum(p.markah for p in dimuat) / len(dimuat))

nama = [p.nama for p in dimuat]
markah = [p.markah for p in dimuat]

plt.bar(nama, markah)
plt.title("Markah Pelajar")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig("fig_projek_v40.png", dpi=150)
plt.close()

uji_tambah()
uji_cari()
uji_purata()
uji_padam()

print("APLIKASI SIAP")
