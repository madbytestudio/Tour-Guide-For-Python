import pandas as pd

df = pd.read_csv("pelajar.csv")

print(df)
print("Purata markah:", df["markah"].mean())
