import numpy as np
import pandas as pd

df = pd.DataFrame({'Col1': [1, np.nan, 3, 4],
                   'Col2': [np.nan, 6, np.nan, 8],
                   'Col3': [9, 10, np.nan, 12]})

print("Checking missing values: ")
print(df.isnull())

print("Drop rows with missing values: ")
df_dropp= df.dropna()
print(df_drop)

print("Fill missing values: ")
df_fill = df.fillna(0)
print(df_fill)

print("Fill missing values with the mean of the column: ")
df_fill_mean = df.fillna(df.mean())
print(df_fill_mean)

print("\nInterpolate missing values: ")
df_interpolate = df.interpolate()
print(df_interpolate)
