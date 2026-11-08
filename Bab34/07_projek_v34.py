from pymongo import MongoClient

class PangkalanPelajar:
    def __init__(self):
        self.klien = MongoClient("mongodb://127.0.0.1:27017")
        self.koleksi = self.klien["tour_guide"]["pelajar_projek"]
        self.koleksi.delete_many({})

    def tambah(self, nama, kursus, markah):
        self.koleksi.insert_one({
            "nama": nama,
            "kursus": kursus,
            "markah": markah,
        })

    def laporan(self):
        for dokumen in self.koleksi.find({}, {"_id": 0}).sort("markah", -1):
            print(f"{dokumen['nama']} - {dokumen['kursus']} - {dokumen['markah']}")

    def purata(self):
        bilangan = self.koleksi.count_documents({})
        if bilangan == 0:
            return 0
        jumlah = sum(d["markah"] for d in self.koleksi.find({}, {"markah": 1}))
        return jumlah / bilangan

    def tutup(self):
        self.klien.close()

sistem = PangkalanPelajar()
sistem.tambah("Aiman Hakim", "Diploma Sains Komputer", 85.5)
sistem.tambah("Siti Aminah", "Diploma Teknologi Maklumat", 90.0)
sistem.tambah("Raj Kumar", "Diploma Multimedia", 78.5)

print("=== LAPORAN PELAJAR ===")
sistem.laporan()
print("Purata:", sistem.purata())
sistem.tutup()
