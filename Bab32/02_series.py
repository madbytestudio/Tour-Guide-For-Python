import pandas as pd

markah = pd.Series([85.5, 90.0, 78.5], index=["Aiman", "Siti", "Raj"])

print(markah)
print("Purata:", markah.mean())
print("Maksimum:", markah.max())
