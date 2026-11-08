from pymongo import MongoClient

klien = MongoClient("mongodb://127.0.0.1:27017")
koleksi = klien["tour_guide"]["pelajar"]

hasil = koleksi.update_one(
    {"nama": "Aiman Hakim"},
    {"$set": {"markah": 90.0}},
)
print("Diubah:", hasil.modified_count)

hasil = koleksi.delete_one({"nama": "Raj Kumar"})
print("Dipadam:", hasil.deleted_count)

for dokumen in koleksi.find({}, {"_id": 0}).sort("nama", 1):
    print(dokumen)

klien.close()
