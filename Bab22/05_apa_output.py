import json
import re

data = {"nama": "Aiman", "aktif": True, "markah": None}

print(json.dumps(data))
print(re.findall(r"\d+", "A1 B22 C333"))
print(re.sub(r"\s+", "-", "Sistem Analisis Pelajar"))
