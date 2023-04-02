import numpy as np
ran_arr = np.random.randn(4, 4)
print(ran_arr)

a = np.array([1, 2, 3])
b = a * 3
print(b)
#Operations on arr
arr1_1 = np.array([10,20])
sum_arr = arr1_1 + arr1_1
print("Sum of arr:",sum_arr)

arr1_1 = np.array([10,20])
mul_arr = arr1_1 * arr1_1
print("mul of arr:",mul_arr)

#slicing
print(arr1_1[0])
print(arr1_1[0:1])

#computing outer product
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.outer(a, b)
print(c)