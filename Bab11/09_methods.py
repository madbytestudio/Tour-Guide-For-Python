pelajar = {"nama": "Aiman", "markah": 85.5}

print(pelajar.get("nama"))
print(pelajar.get("umur", "Tiada data"))
print(pelajar.keys())
print(pelajar.values())
print(pelajar.items())

pelajar.setdefault("semester", 3)
print(pelajar)
