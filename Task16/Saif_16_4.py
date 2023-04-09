import pandas as pd

df = pd.DataFrame({'A': ['Hy', 'hello', 'Hy', 'hello', 'Hy', 'hello', 'Hy', 'Hy'],
                   'B': ['four', 'four', 'three', 'three', 'two', 'three', 'four', 'two'],
                   'C': [1, 2, 3, 4, 5, 6, 7, 8],
                   'D': [10, 20, 30, 40, 50, 60, 70, 80]})

stacked_df = df.stack() #Use stack to pivot 'wide' dataframe to 'long' dataframe....
print(stacked_df)

unstacked_df = stacked_df.unstack() #Use unstack to pivot 'long' dataframe back to 'wide' dataframe...
print(unstacked_df)

unstacked_df = stacked_df.unstack().stack() #Use stack to pivot 'wide' dataframe back to 'long' dataframe...
print(unstacked_df)


