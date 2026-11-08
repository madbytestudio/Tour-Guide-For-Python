asal = {"nama": "Aiman", "markah": 85.5}
salinan = asal.copy()
rujukan = asal

salinan["markah"] = 90.0
rujukan["semester"] = 3

print("asal:", asal)
print("salinan:", salinan)
print("rujukan:", rujukan)
