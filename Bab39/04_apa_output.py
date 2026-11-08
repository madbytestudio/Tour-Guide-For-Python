import json

data = {"nama": "Aiman", "markah": 85.5}
teks = json.dumps(data)

print(teks)
print(json.loads(teks)["nama"])
