import numpy as np
from scipy.linalg import lu

# Define your matrix
A = np.array([
    [2.0, 1.0, -1.0],
    [-3.0, -1.0, 2.0],
    [-2.0, 1.0, 2.0]
])

print("Original matrix A:")
print(A)

# Perform LU decomposition with partial pivoting
# This is the professional, industry-standard method
P, L, U = lu(A)

print("\nResult from SciPy's lu() function (with Pivoting):")
print("P (Permutation matrix - records row swaps):")
print(P)
print("L (Lower triangular):")
print(L)
print("U (Upper triangular):")
print(U)

# Verify the decomposition: P * A = L * U
print("\nVerification: P * A should equal L * U")
print("P * A =")
print(P @ A) # Matrix multiplication
print("L * U =")
print(L @ U)
