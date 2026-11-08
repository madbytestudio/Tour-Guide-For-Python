pelajar = {"nama": "Aiman", "kursus": "DSC", "semester": 3, "markah": 85.5}

pelajar.pop("semester")
print(pelajar)

pelajar.popitem()
print(pelajar)

del pelajar["kursus"]
print(pelajar)

pelajar.clear()
print(pelajar)
