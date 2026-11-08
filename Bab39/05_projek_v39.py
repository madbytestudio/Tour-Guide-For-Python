import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from _app import Pelajar, SistemAnalisis, simpan, muat

sistem = SistemAnalisis()
sistem.tambah(Pelajar("Aiman Hakim", "Diploma Sains Komputer", 3, 85.5, 90))
sistem.tambah(Pelajar("Siti Aminah", "Diploma Teknologi Maklumat", 3, 90.0, 95))
sistem.tambah(Pelajar("Raj Kumar", "Diploma Multimedia", 3, 78.5, 80))

simpan(sistem.senarai, "data_pelajar.json")
dimuat = muat("data_pelajar.json")

sistem2 = SistemAnalisis()
for p in dimuat:
    sistem2.tambah(p)

print("=== LAPORAN ===")
sistem2.laporan()
print("Purata:", sistem2.purata())

nama = [p.nama for p in sistem2.senarai]
markah = [p.markah for p in sistem2.senarai]

plt.bar(nama, markah)
plt.title("Markah Pelajar")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig("fig_projek_v39.png", dpi=150)
plt.close()

print("Carta projek disimpan.")
