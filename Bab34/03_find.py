from pymongo import MongoClient

klien = MongoClient("mongodb://127.0.0.1:27017")
koleksi = klien["tour_guide"]["pelajar"]

for dokumen in koleksi.find({}, {"_id": 0}):
    print(dokumen)

klien.close()
