import numpy as np

def generate_linear_system(n, value_range=(-5, 5)):
    """
    Generates a random linear system A*x = b with integer entries.
    The matrix A is made diagonally dominant to ensure it is non-singular and well-conditioned.

    Args:
        n: Size of the matrix (n x n) and vector (n x 1).
        value_range: Tuple (min, max) for the random integer values in A.

    Returns:
        A: Generated n x n matrix (diagonally dominant, integers).
        b: Right-hand side vector n x 1.
        x_known: The known solution vector (integers).
    """
    min_val, max_val = value_range
    
    # Step 1: Generate a known solution vector x_known with random integers
    x_known = np.random.randint(min_val, max_val + 1, size=n)
    
    # Step 2: Generate a random matrix A with integers
    A = np.random.randint(min_val, max_val + 1, size=(n, n))
    
    # Step 3: Make the matrix A diagonally dominant
    for i in range(n):
        # Calculate the sum of absolute values of non-diagonal elements in the row
        row_sum = np.sum(np.abs(A[i])) - np.abs(A[i, i])
        # Set the diagonal element to be larger than that sum
        # We add a random positive integer (1 to 5) to ensure strong dominance
        A[i, i] = row_sum + np.random.randint(1, 6)
    
    # Step 4: Compute the right-hand side vector b
    b = A @ x_known  # Matrix multiplication
    
    return A, b, x_known

# --- Example: Generate and test a system ---
# Set a seed for reproducible results (optional)
np.random.seed(42)

# Generate a 3x3 system
n = 3
A, b, x_known = generate_linear_system(n)

print("Generated Linear System A * x = b")
print("\nKnown Solution Vector x_known:")
print(x_known)
print("\nGenerated Matrix A (Diagonally Dominant):")
print(A)
print("\nComputed Right-Hand Side b = A * x_known:")
print(b)

# --- Let's verify it's diagonally dominant ---
print("\nVerifying Diagonal Dominance:")
for i in range(n):
    diagonal = np.abs(A[i, i])
    off_diagonal_sum = np.sum(np.abs(A[i])) - diagonal
    print(f"Row {i}: |{A[i, i]}| = {diagonal} > {off_diagonal_sum} = Σ|a_ij| (j≠i) -> {diagonal > off_diagonal_sum}")

# --- Test with NumPy's solver ---
x_calculated = np.linalg.solve(A, b)

print("\nTesting with NumPy's np.linalg.solve:")
print(f"Calculated solution: {x_calculated}")
print(f"Known solution:      {x_known}")
print(f"Absolute error:      {np.abs(x_calculated - x_known)}")
print(f"Total error (L2 norm): {np.linalg.norm(x_calculated - x_known):.2e}")
