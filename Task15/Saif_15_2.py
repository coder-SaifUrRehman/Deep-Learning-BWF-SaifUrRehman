import pandas as pd
import numpy as np

df = pd.DataFrame({'Col1': [1, np.nan, 3, 4],
                   'Col2': [np.nan, 6, np.nan, 8],
                   'Col3': [9, 10, np.nan, 12]})

print(df)

print("Drop rows: ")
df_drop = df.dropna(how='all')
print(df_drop)

print("Drop columns: ")
df_drop_col = df.dropna(how='all', axis=1)
print(df_drop_col)
