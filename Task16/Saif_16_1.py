import pandas as pd


df1 = pd.DataFrame({'key': ['A', 'B', 'C', 'D'],
                    'value1': [1, 2, 3, 4],
                    'value2': [10, 20, 30, 40]})
df2 = pd.DataFrame({'key': ['B', 'D', 'E', 'F'],
                    'value1': [5, 6, 7, 8],
                    'value2': [50, 60, 70, 80]})
             
print("DF1:\n ", df1)
print("DF2:\n ", df2)

merged_df = pd.merge(df1, df2, on='key', how='outer')  #Merge dataframes on the 'key' col
print(merged_df)

concat_df = pd.concat([df1, df2], axis=0) #Concatenate dataframes along the rows
print(concat_df)

df3 = pd.DataFrame({'key': [ 'D', 'E', 'F', 'G'],
                    'value1': [8, 9, 10, None],
                    'value2': [80, 90, 100, None]})
                    
print("Dataframe 3:\n ", df3)                   

print("Combine df1 and df3, fill missing values in df1 with values from df3: ")
combined_df = df1.combine_first(df3)
print(combined_df)
