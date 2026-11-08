import json

data = {
    "teks": "Aiman",
    "nombor": 20,
    "perpuluhan": 85.5,
    "boolean": True,
    "tiada": None,
    "senarai": [1, 2, 3],
}

print(json.dumps(data, indent=2))
