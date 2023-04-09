import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob


path = r'D:\Bytewise Fellowship\BWT-Tasks-Saifi\MIini_Project#01\US_Census Data Cleaning'
files = glob.glob(path + "/*.csv")
dfs = []
for file in files:
    df = pd.read_csv(file, header=0)
    dfs.append(df)

us_census = pd.concat(dfs, axis=0, ignore_index=True)
# print(us_census)

# Print the columns and data types of the merged dataframe
print("Columns:")
print(us_census.columns)
print("DataTypes: ")
print(us_census.dtypes)

# Select the non-numerical columns and print their names
non_numeric_col = us_census.select_dtypes(exclude=['int64', 'float64']).columns.tolist()
print("Non Numeric Columns: ")
print(non_numeric_col)

print("Print the first five rows of the merged dataframe..")
print(us_census.head())


us_census['GenderPop'].fillna(value='0', inplace=True) # Fill any missing values in the 'GenderPop' column with '0'

us_census[['Men', 'Women']] = us_census['GenderPop'].str.split('_', expand=True)# Split the GenderPop column into Men and Women columns

us_census['Men'] = us_census['Men'].replace('[^0-9]', '', regex=True).astype(int) # Remove non-numeric characters and the M/F character from the Men and Women columns

us_census['Women'] = us_census['Women'].replace('[^0-9]', '', regex=True) # Remove non-numeric characters and convert to int

us_census['Women'] = pd.to_numeric(us_census['Women'], errors='coerce')
us_census['Women'] = us_census['Women'].fillna(0).astype(int)

# Remove the M/F character from the Men and Women columns
us_census['Men'] = us_census['Men'].replace('M', '', regex=True).astype(int)
us_census['Women'] = us_census['Women'].replace('F', '', regex=True).astype(int)

# Drop the original GenderPop column
us_census = us_census.drop(columns=['GenderPop'])


# Make scatterplot
plt.scatter(us_census['Women'], us_census['Income'])
plt.xlabel('Women')
plt.ylabel('Income')
plt.show()

# Convert 0 to NaN in Women column
us_census['Women'] = us_census['Women'].replace(0, np.nan)

# Fill NaN values in men column
us_census['Women'] = us_census['Women'].fillna(us_census['TotalPop'] - us_census['Men'])
print(us_census['Women'])
import matplotlib.pyplot as plt

# Convert columns to numerical format
us_census['Hispanic'] = us_census['Hispanic'].replace('[%]', '', regex=True).astype(float)
us_census['White'] = us_census['White'].replace('[%]', '', regex=True).astype(float)
us_census['Black'] = us_census['Black'].replace('[%]', '', regex=True).astype(float)
us_census['Native'] = us_census['Native'].replace('[%]', '', regex=True).astype(float)
us_census['Asian'] = us_census['Asian'].replace('[%]', '', regex=True).astype(float)
us_census['Pacific'] = us_census['Pacific'].replace('[%]', '', regex=True).astype(float)

# Fill nan values with mean of column
us_census = us_census.fillna(value={'Hispanic':us_census['Hispanic'].mean(),
                                    'White':us_census['White'].mean(),
                                    'Black':us_census['Black'].mean(),
                                    'Native':us_census['Native'].mean(),
                                    'Asian':us_census['Asian'].mean(),
                                    'Pacific':us_census['Pacific'].mean()})

# Check duplicates
duplicates = us_census.duplicated()
print(duplicates.value_counts())

# Create histograms

us_census.plot.hist(x="State", y="Pacific" , title="Pacific Population...",color=[
         'orange'])
plt.show(block=True)

us_census.plot.hist(x="State", y="White" , title="White Population...",color=[
         'orange'])
plt.show(block=True)

us_census.plot.hist(x="State", y="Black" , title="Black Population...",color=[
         'orange'])
plt.show(block=True)

plt.hist(us_census['Hispanic'], bins=10)
plt.title('Hispanic Population...')
plt.xlabel('Percentage')
plt.ylabel('Frequency')
plt.show()

plt.hist(us_census['Native'], bins=10)
plt.title('Native Population...')
plt.xlabel('Percentage')
plt.ylabel('Frequency')
plt.show()

us_census.plot.hist(x="State", y="Asian" , title="Asian Population...",color=[
         'orange'])
plt.show(block=True)


us_census.to_excel('US-census-final-modified.xlsx', index=False)
