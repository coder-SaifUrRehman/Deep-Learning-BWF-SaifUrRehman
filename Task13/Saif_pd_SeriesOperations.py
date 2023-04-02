import pandas as pd
s1 = pd.Series([5,4,3,2,1])
s2 = pd.Series([1,2,3,4,5])

Filtering = s1 > 3
print("Filering\n",s1[Filtering]) 


print('addition\n',s1 + s2) 
print('substraction\n',s2 - s1) 
print ('multiplication\n',s2 * s1) 
