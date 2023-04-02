import numpy as np

#Broadcasting describes how NumPy treats arrays with different shapes during arithmetic operations...

a = np.array([1, 2, 3])
c = a + 5  #Adding a Scalar to an Array
print(c)

c = a - 2 #Subtracting a Scalar from an Array
print(c)

c = a * 3 #Multiplying a Scalar with an Array
print(c)

c = a / 3 #Dividing an Array by a Scalar
print(c)



a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

c = a + b  #Adding Two Arrays with the Same Shape
print(c)

c = a * b #Multiplying Two Arrays with the Same Shape
print(c)


a = np.array([1, 2, 3])
b = np.array([4])
c = a + b #Adding Two Arrays with Different Sizes
print(c)


a = np.array([1, 2, 3])
b = np.array([[4, 5, 6], [7, 8, 9]])
c = a[:, np.newaxis] + b.T #Adding Two Arrays with Different Number of Dimensions
print(c)


a = np.array([[1], [2], [3]])
b = np.array([4, 5, 6])

c = a * b #Multiplying Two Arrays with Different Shapes
print(c)


a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

c = np.outer(a, b) #Computing Outer Product of Two Arrays
print(c)

a = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
b = np.array([1, 2])

c = a + b[:, np.newaxis, np.newaxis]  #Broadcasting in Higher Dimensions
print(c)


a = np.zeros((3, 3))
b = np.array([1, 2, 3])
a[:, :] = b[:, np.newaxis] #Setting Array Values by Broadcasting
print(a)

