import pandas as pd

my_dict = {'name':['Saifi', 'Ahmed', 'Ali'],
    'age' : [21, 20, 22],
    'city' : ['BWP ', 'ISL ', 'LAH']}


df = pd.DataFrame(my_dict) # Creating DataFrame from the dictionary
print(df)
print(df['name']) # Access a column by name
print(df.loc[2]) # Access a row by index
print(df.loc[1, 'name']) # Access a cell by row and column

df['Country'] = ['pak', 'pk', 'pkk'] # Modifying/Adding a new column
print(df)

df = df.drop('Country', axis= 1) #removing a col.
print(df)

df_filtered = df[df['age']<22] # Filtering rows by age.
print(df_filtered)

df_sorted = df.sort_values('age', ascending = False) # Sorting row by age in descending order
print(df_sorted)

