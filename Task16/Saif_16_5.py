import pandas as pd

series_ = pd.Series([1, 2, 3, 4, 5], index=pd.Index(['a', 'b', 'c', 'd', 'e'], name='letters'))
df = pd.DataFrame({'left': series_, 'right': series_ + 5}, columns=pd.Index(['left', 'right'], name='side'))

print(df)

