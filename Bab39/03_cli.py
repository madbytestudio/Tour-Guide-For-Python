import argparse
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from _app import Pelajar, SistemAnalisis, muat


def data_contoh():
    sistem = SistemAnalisis()
    sistem.tambah(Pelajar("Aiman Hakim", "Diploma Sains Komputer", 3, 85.5, 90))
    sistem.tambah(Pelajar("Siti Aminah", "Diploma Teknologi Maklumat", 3, 90.0, 95))
    sistem.tambah(Pelajar("Raj Kumar", "Diploma Multimedia", 3, 78.5, 80))
    return sistem


def jana_carta(sistem):
    nama = [p.nama for p in sistem.senarai]
    markah = [p.markah for p in sistem.senarai]
    plt.bar(nama, markah)
    plt.title("Markah Pelajar")
    plt.xticks(rotation=15)
    plt.tight_layout()
    plt.savefig("fig_cli.png", dpi=150)
    plt.close()
    print("fig_cli.png disimpan.")


parser = argparse.ArgumentParser()
parser.add_argument("command", nargs="?", default="laporan", choices=["laporan", "carta"])
args = parser.parse_args()

try:
    pelajar = muat("data_pelajar.json")
    sistem = SistemAnalisis()
    for p in pelajar:
        sistem.tambah(p)
except FileNotFoundError:
    sistem = data_contoh()

if args.command == "laporan":
    sistem.laporan()
    print("Purata:", sistem.purata())
else:
    jana_carta(sistem)
