import pandas as pd
import numpy as np


df = pd.DataFrame({'Col1': [1, np.nan, 3, 4],
                   'Col2': [np.nan, 6, np.nan, 8],
                   'Col3': [9, 10, np.nan, 12]})


print("Fill missing values with last observed value, limit to 2 consecutive missing values: ")
df_filled = df.fillna(method='ffill', limit=2)
print(df_filled)

print("Fill missing values with mean of the column, modifying the object: ")
df.fillna(df.mean(), inplace=True)
print(df)
