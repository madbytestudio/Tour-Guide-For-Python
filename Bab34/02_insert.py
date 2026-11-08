from pymongo import MongoClient

klien = MongoClient("mongodb://127.0.0.1:27017")
db = klien["tour_guide"]
koleksi = db["pelajar"]

koleksi.delete_many({})

data = [
    {"nama": "Aiman Hakim", "kursus": "Diploma Sains Komputer", "markah": 85.5},
    {"nama": "Siti Aminah", "kursus": "Diploma Teknologi Maklumat", "markah": 90.0},
    {"nama": "Raj Kumar", "kursus": "Diploma Multimedia", "markah": 78.5},
]

hasil = koleksi.insert_many(data)

print("ID:", hasil.inserted_ids)
print("Bilangan:", koleksi.count_documents({}))

klien.close()
