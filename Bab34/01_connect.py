from pymongo import MongoClient

klien = MongoClient("mongodb://127.0.0.1:27017", serverSelectionTimeoutMS=5000)

print(klien.admin.command("ping"))
print(klien.list_database_names())

klien.close()
