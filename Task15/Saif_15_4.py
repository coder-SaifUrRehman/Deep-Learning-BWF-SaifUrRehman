import pandas as pd
import numpy as np

df = pd.DataFrame({'Col1': ['Hy', 'Hy', 'Hy', 'hello', 'are', 'you', 'you'],
                   'Col2': ['Hy', 'Hy', 'two', 'two', 'one', 'one', 'two'],
                   'Col3': ['Hy', 'Hy', 3, 4, 5, np.nan, 7],
                   'Col4': ['Hy', 'Hy', 10, 11, 12, 13, 14]})

print (df)

print("Checking for duplicate rows: ")
print(df.duplicated())

print("Drop duplicate rows: ")
df_new = df.drop_duplicates()
print(df_new)
