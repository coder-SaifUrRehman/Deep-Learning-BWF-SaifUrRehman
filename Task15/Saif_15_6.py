import numpy as np
import pandas as pd

np.random.seed(123)
data = pd.DataFrame({'A': np.random.normal(0, 1, 40),
                     'B': np.random.normal(0, 1, 40),
                     'C': np.random.normal(0, 1, 40)})

col = data['C'] #single col
threshold = 0.5
print("Original column:\n", col)

col_filtered = col[np.abs(col) <= threshold] # filter out the outliers in selected col
print("Filtered column:\n", col_filtered)

col_filtered1 = col.loc[np.abs(col) <= threshold] # use the .loc accessor to filter out the outliers in selected col
print("Filtered column (.loc):\n", col_filtered1)
