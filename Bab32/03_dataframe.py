import pandas as pd

data = {
    "nama": ["Aiman", "Siti", "Raj"],
    "kursus": ["DSC", "DIT", "DMM"],
    "markah": [85.5, 90.0, 78.5],
}

df = pd.DataFrame(data)

print(df)
print(df.columns.tolist())
print(df["markah"].mean())
