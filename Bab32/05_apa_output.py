import numpy as np
import pandas as pd

markah = np.array([80, 90, 100])
print(markah.mean())

df = pd.DataFrame({"markah": markah})
print(df["markah"].sum())
