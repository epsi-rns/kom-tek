import numpy as np

def doolittle_lu_decomposition(A):
    """
    Performs LU decomposition on matrix A using Doolittle's method.
    Returns L (with 1's on diagonal) and U such that A = L * U.
    """
    n = len(A)
    # Initialize L as identity matrix and U as zero matrix
    L = np.eye(n)  # Identity matrix (1's on diagonal, 0's elsewhere)
    U = np.zeros((n, n))
    
    print("Starting Doolittle LU Decomposition")
    print("Initial L matrix:\n", L)
    print("Initial U matrix:\n", U)
    print("-" * 50)
    
    # Decomposition process
    for k in range(n):  # For each row/column
        print(f"Step {k+1}: Processing row/column {k}")
        
        # Calculate elements of the k-th row of U
        for j in range(k, n):
            print(f"  Calculating U[{k},{j}]")
            sum_val = 0.0
            # Summation: Σ (L[k][m] * U[m][j]) for m=0 to k-1
            for m in range(k):
                print(f"    Adding L[{k},{m}] * U[{m},{j}] = {L[k,m]} * {U[m,j]}")
                sum_val += L[k, m] * U[m, j]
            
            U[k, j] = A[k, j] - sum_val
            print(f"    U[{k},{j}] = A[{k},{j}] - sum = {A[k,j]} - {sum_val} = {U[k,j]}")
        
        # Calculate elements of the k-th column of L (for i > k)
        for i in range(k+1, n):
            print(f"  Calculating L[{i},{k}]")
            sum_val = 0.0
            # Summation: Σ (L[i][m] * U[m][k]) for m=0 to k-1
            for m in range(k):
                print(f"    Adding L[{i},{m}] * U[{m},{k}] = {L[i,m]} * {U[m,k]}")
                sum_val += L[i, m] * U[m, k]
            
            L[i, k] = (A[i, k] - sum_val) / U[k, k]
            print(f"    L[{i},{k}] = (A[{i},{k}] - sum) / U[{k},{k}] = ({A[i,k]} - {sum_val}) / {U[k,k]} = {L[i,k]}")
        
        print(f"After step {k+1}:")
        print("L =\n", L)
        print("U =\n", U)
        print("-" * 50)
    
    return L, U

# Test with our 2x2 example
#A = np.array([[2.0, 1.0],
#              [1.0, 3.0]])

# Test with our 3x3 example
A = np.array([
    [2, 1, -1],
    [-3, -1, 2],
    [-2, 1, 2]
])

print("Original matrix A:")
print(A)
print()

# Perform LU decomposition
L, U = doolittle_lu_decomposition(A)

print("Final Result:")
print("L matrix (lower triangular with 1's on diagonal):")
print(L)
print("U matrix (upper triangular):")
print(U)
print()

# Verify the decomposition
print("Verification: L * U should equal A")
print("L * U =")
print(np.dot(L, U))
print("Original A =")
print(A)
