import numpy as np
from statistics import mode


arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([2, 4, 6, 8, 10])

# calculating   mean
mean = np.mean(arr1)
print("Mean:", mean)

# calculating   median
median = np.median(arr1)
print("Median:", median)

# Calculating   mode  by using statistics module
print("Mode of a:")
print(mode(arr1))

# calculating   standard deviation
std_dev = np.std(arr1)
print("Standard Deviation:", std_dev)

# calculating   variance
variance = np.var(arr1)
print("Variance:", variance)

# calculating   50th percentile
percentile = np.percentile(arr1, 50)
print("50th Percentile:", percentile)

# calculating   correlation coefficient
corr_coeff = np.corrcoef(arr1, arr2)[0, 1]
print("Correlation Coefficient:", corr_coeff)
