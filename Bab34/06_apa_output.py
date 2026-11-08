from pymongo import MongoClient

klien = MongoClient("mongodb://127.0.0.1:27017")
koleksi = klien["tour_guide"]["pelajar"]

print("Bilangan:", koleksi.count_documents({}))
print("Pelajar pertama:", koleksi.find_one({}, {"_id": 0}))

klien.close()
