import json
import re

pelajar = [
    {"nama": "Aiman Hakim", "kod_kursus": "DSC-2026", "markah": 85.5},
    {"nama": "Siti Aminah", "kod_kursus": "DIT-2026", "markah": 90.0},
    {"nama": "Raj Kumar", "kod_kursus": "dm-26", "markah": 78.5},
]

corak = r"^[A-Z]{3}-\d{4}$"

print(json.dumps(pelajar, indent=2, ensure_ascii=False))
print()

for rekod in pelajar:
    sah = re.match(corak, rekod["kod_kursus"]) is not None
    print(rekod["nama"], "-", rekod["kod_kursus"], "- Sah:", sah)
