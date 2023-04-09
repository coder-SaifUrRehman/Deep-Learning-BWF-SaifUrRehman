import pandas as pd


df1 = pd.DataFrame({'key': ['A', 'B', 'C', 'D'],
                    'value1': [1, 2, 3, 4],
                    'value2': [10, 20, 30, 40]})
df2 = pd.DataFrame({'key': ['B', 'D', 'E', 'F'],
                    'value1': [5, 6, 7, 8],
                    'value2': [50, 60, 70, 80]})
             
print("DF1:\n ", df1)
print("DF2:\n ", df2)


print("\nMerge dataframes on the 'key' column using different join type... ")
inner_join_df = pd.merge(df1, df2, on='key', how='inner')
left_join_df = pd.merge(df1, df2, on='key', how='left')
right_join_df = pd.merge(df1, df2, on='key', how='right')
outer_join_df = pd.merge(df1, df2, on='key', how='outer')


print("Inner join:")
print(inner_join_df)
print("Left join:")
print(left_join_df)
print("Right join:")
print(right_join_df)
print("Outer join:")
print(outer_join_df)
