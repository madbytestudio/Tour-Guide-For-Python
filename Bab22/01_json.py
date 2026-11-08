import json

pelajar = {
    "nama": "Aiman Hakim",
    "kursus": "Diploma Sains Komputer",
    "semester": 3,
    "markah": 85.5,
    "lulus": True,
}

teks_json = json.dumps(pelajar, indent=2, ensure_ascii=False)
print(teks_json)

kembali = json.loads(teks_json)
print(kembali["nama"])
print(type(kembali))
