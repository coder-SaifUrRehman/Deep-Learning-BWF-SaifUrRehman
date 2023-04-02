import pandas as pd


df = pd.read_csv('MOCK_DATA.json') # Load data from a CSV file
print(df.head())
df.describe()
df.info()

