import pandas as pd

data = {'name': ['Saifi', 'Umer', 'ikun'],
        'country': ['Pakistan', 'Afg', 'China'],
        'city': ['Bahawalpur', 'Chamman', 'wuhan']}
df = pd.DataFrame(data)

print("Select column based on label")
print(df.loc[:, 'name']) # loc allows you to select rows and columns by their index or key.

print("Select multiple columns by key") 
print(df.loc[:, ['name', 'city']])

print("Select row by index postion")

print(df.iloc[1]) # iloc allows you to select rows and columns by integer position

print("Select multiple row based on index postion")
print(df.iloc[[0, 1]])


