import pandas as pd

data = [1,2,3,4]
index = ['a', 'b', 'c', 'd']
s = pd.Series(data, index=index)
print(s)
print(s.values)
print(s.index)



s = pd.Series([10,20,30,40,50], index=['a','b','c','d','e'])
print(s)

s.index = [1,2,3,4,5]  # Alter the series index
print("Series  with modified Index: ")
print(s)
print(s.loc['a'])  # access element by label
print(s.iloc[0])  # access element by position




