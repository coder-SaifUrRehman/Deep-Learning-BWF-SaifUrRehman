import numpy as np

#NumPy internally stores data in a contiguous block of memory, independent of other built-in Python objects. 
#NumPy operations perform complex computations on entire arrays without the need for Python for loops.

arr1  = np.array([1000]) #create an array with given element....
print(arr1)
print(type(arr1))

arr1_2=np.zeros(4)
print(arr1_2)

arr2 = np.arange(10) #create an array of given range-1....
print(arr2)
print(type(arr2))
#print(arr2.shape())


Two_dim_array = np.array([[1,2,3],[4,5,6]])
print(Two_dim_array)





    
