import pandas as pd

df1 = pd.DataFrame({'key': ['A', 'B', 'C', 'D'],
                    'value1': [1, 2, 3, 4],
                    'value2': [10, 20, 30, 40]})
df2 = pd.DataFrame({'key': ['B', 'D', 'E', 'F'],
                    'value1': [5, 6, 7, 8],
                    'value2': [50, 60, 70, 80]})

print("Merge the dataframes on the 'key' col with suffixes: ")
merged_df = pd.merge(df1, df2, on='key', suffixes=('-left', '-right'))
print(merged_df)
