import numpy as np

def doolittle(A):
    """
    Vanilla Doolittle LU decomposition without pivoting.
    For educational use. Not numerically robust.
    """
    n = len(A)
    L = np.eye(n)
    U = np.zeros((n, n))
    
    for k in range(n):
        # Calculate k-th row of U
        for j in range(k, n):
            U[k, j] = A[k, j] - np.sum(L[k, :k] * U[:k, j])
        # Calculate k-th column of L
        for i in range(k+1, n):
            L[i, k] = (A[i, k] - np.sum(L[i, :k] * U[:k, k])) / U[k, k]
    return L, U

A = np.array([
    [2.0, 1.0, -1.0],
    [-3.0, -1.0, 2.0],
    [-2.0, 1.0, 2.0]
], dtype=float)

L, U = doolittle(A)

print("L:\n", L)
print("U:\n", U)
print("A - L*U:\n", A - L @ U) # Should be near zero
