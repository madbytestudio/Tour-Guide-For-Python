def log(function):
    def wrapper(*args, **kwargs):
        print("[LOG] Menjalankan", function.__name__)
        hasil = function(*args, **kwargs)
        print("[LOG] Selesai", function.__name__)
        return hasil
    return wrapper

@log
def kira_purata(markah):
    return sum(markah) / len(markah)

def jana_laporan(pelajar):
    for rekod in pelajar:
        yield f"{rekod['nama']} - {rekod['markah']}"

pelajar = [
    {"nama": "Aiman Hakim", "markah": 85.5},
    {"nama": "Siti Aminah", "markah": 90.0},
    {"nama": "Raj Kumar", "markah": 78.5},
]

print("Purata:", kira_purata([85.5, 90.0, 78.5]))

for baris in jana_laporan(pelajar):
    print(baris)
