import numpy as np

# Create two matrices
m1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 7]])
m2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

# summing the matrices
matrix_sum = m1 + m2
print("Matrix Addition:\n", matrix_sum)


# Multiplying the matrices
matrix_prod = m1 @ m2
print("Matrix Multiplication:\n", matrix_prod)

# Transpose of matrix
matrix_trans = m1.T
print("Matrix Transpose:\n", matrix_trans)

# calculating the determinant
m_det = np.linalg.det(m1)
print("Matrix Determinant:", m_det)

# calculating the inverse
m_inv = np.linalg.inv(m1)
print("Matrix Inverse:\n", m_inv)

# calculating the rank
m_rank = np.linalg.matrix_rank(m1)
print("Matrix Rank:", m_rank)  

# calculating the eigenvalues and eigenvectors
m_eig = np.linalg.eig(m1)
print("Eigenvalues and Eigenvectors:\n", m_eig)


# Solving the equations
eq1 = np.array([[1,2],[4,5]])
eq2 = np.array([7,5])
x = np.linalg.solve(eq1, eq2)
print("Solutions to Equations:", x)
  