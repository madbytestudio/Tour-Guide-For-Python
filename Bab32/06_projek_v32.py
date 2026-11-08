import pandas as pd

data = [
    {"nama": "Aiman", "kursus": "DSC", "markah": 85.5},
    {"nama": "Siti", "kursus": "DIT", "markah": 90.0},
    {"nama": "Raj", "kursus": "DMM", "markah": 78.5},
    {"nama": "Mei", "kursus": "DSC", "markah": 88.0},
]

df = pd.DataFrame(data)

print(df)
print()
print("Purata keseluruhan:", df["markah"].mean())
print("Markah tertinggi:", df["markah"].max())
print()
print(df.sort_values("markah", ascending=False))
print()
print(df.groupby("kursus")["markah"].mean())
