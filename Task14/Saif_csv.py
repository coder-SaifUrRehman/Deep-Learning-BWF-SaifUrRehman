import pandas as pd


df = pd.read_csv('MOCK_DATA.csv') # Load data from a CSV file
print(df.head())
df.describe()
df.info()

print("Reading data from csv file: ")
df = pd.read_csv('MOCK_DATA.csv', header=0, usecols=["first_name"], nrows=2, delimiter=',')
print(df)

