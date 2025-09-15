import sympy as sp

# Define the matrix A with symbolic entries
A = sp.Matrix([
    [2, 1, -1],
    [-3, -1, 2],
    [-2, 1, 2]
])

print("Original matrix A:")
sp.pprint(A)
print()

n = A.rows
# Initialize L as an identity matrix and U as a zero matrix
L = sp.eye(n)
U = sp.zeros(n)

print("Starting Doolittle LU Decomposition")
print("Initial L matrix:")
sp.pprint(L)
print("Initial U matrix:")
sp.pprint(U)
print("-" * 50)

# Doolittle's Algorithm
for k in range(n):
    print(f"Step {k+1}: Processing row/column {k}")
    
    # Calculate the k-th row of U
    for j in range(k, n):
        print(f"  Calculating U[{k},{j}]")
        # Summation: Σ (L[k, m] * U[m, j]) for m=0 to k-1
        sum_val = 0
        for m in range(k):
            sum_val += L[k, m] * U[m, j]
            print(f"    Adding L[{k},{m}] * U[{m},{j}] = {L[k,m]} * {U[m,j]} = {L[k,m] * U[m,j]}")
        
        U[k, j] = A[k, j] - sum_val
        print(f"    U[{k},{j}] = A[{k},{j}] - sum = {A[k,j]} - {sum_val} = {U[k,j]}")
    
    # Calculate the k-th column of L (for i > k)
    for i in range(k+1, n):
        print(f"  Calculating L[{i},{k}]")
        # Summation: Σ (L[i, m] * U[m, k]) for m=0 to k-1
        sum_val = 0
        for m in range(k):
            sum_val += L[i, m] * U[m, k]
            print(f"    Adding L[{i},{m}] * U[{m},{k}] = {L[i,m]} * {U[m,k]} = {L[i,m] * U[m,k]}")
        
        L[i, k] = (A[i, k] - sum_val) / U[k, k]
        print(f"    L[{i},{k}] = (A[{i},{k}] - sum) / U[{k},{k}] = ({A[i,k]} - {sum_val}) / {U[k,k]} = {L[i,k]}")
    
    print(f"After step {k+1}:")
    print("L =")
    sp.pprint(L)
    print("U =")
    sp.pprint(U)
    print("-" * 50)

print("Final Result:")
print("L matrix (lower triangular with 1's on diagonal):")
sp.pprint(L)
print("U matrix (upper triangular):")
sp.pprint(U)
print()

# Verification
print("Verification: L * U should equal A")
print("L * U =")
sp.pprint(L * U)
print("Original A =")
sp.pprint(A)
print(f"Decomposition is correct: {L * U == A}")
