from pymongo import MongoClient

klien = MongoClient("mongodb://127.0.0.1:27017")
koleksi = klien["tour_guide"]["pelajar"]

for dokumen in koleksi.find({"markah": {"$gte": 80}}, {"_id": 0}).sort("markah", -1):
    print(dokumen)

klien.close()
