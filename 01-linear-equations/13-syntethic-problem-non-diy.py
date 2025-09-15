import numpy as np
from scipy import linalg

def generate_linear_system_pro(n, condition_number=100, value_range=(-10, 10)):
    """
    Generates a random linear system A*x = b with a controlled condition number.
    This is a professional, robust method using matrix factorization.

    Args:
        n: Size of the matrix (n x n) and vector (n x 1).
        condition_number: Desired condition number (kappa) for matrix A.
                         Larger kappa means more ill-conditioned (default 100 is well-conditioned).
        value_range: Tuple (min, max) for the random integer values in the known solution x_known.

    Returns:
        A: Generated n x n matrix (invertible, with controlled condition number).
        b: Right-hand side vector n x 1.
        x_known: The known solution vector (integers).
    """
    min_val, max_val = value_range
    
    # Step 1: Generate a known solution vector x_known with random integers
    x_known = np.random.randint(min_val, max_val + 1, size=n)
    
    # Step 2: Generate a well-controlled random matrix A
    # This method creates a matrix with a specific condition number
    # Generate random orthogonal matrices U and V using QR decomposition of random arrays
    U, _ = linalg.qr(np.random.randn(n, n))
    V, _ = linalg.qr(np.random.randn(n, n))
    
    # Create a diagonal matrix D with logarithmically spaced singular values
    # This gives us precise control over the condition number
    s = np.logspace(0, np.log10(condition_number), n)
    D = np.diag(s)
    
    # Construct A = U * D * V^T. This matrix has condition number = condition_number.
    A = U @ D @ V.T
    
    # Step 3: Scale the matrix to have "nice" integer-like values (optional)
    # We scale the matrix to make the values more human-readable
    A = np.round(A * 10) / 10  # Round to 1 decimal place for readability
    
    # Step 4: Compute the right-hand side vector b
    b = A @ x_known  # Matrix multiplication
    
    return A, b, x_known

# --- Example: Generate and analyze a system ---
np.random.seed(42)  # For reproducible results

# Generate a 3x3 system with controlled condition number
n = 3
A, b, x_known = generate_linear_system_pro(n, condition_number=100)

print("Professionally Generated Linear System A * x = b")
print("\nKnown Solution Vector x_known:")
print(x_known)
print("\nGenerated Matrix A:")
print(A)
print("\nComputed Right-Hand Side b = A * x_known:")
print(b)

# --- Analyze the generated matrix ---
print("\nMatrix Analysis:")
# Calculate the actual condition number
cond_number = np.linalg.cond(A)
print(f"Condition number (kappa) of A: {cond_number:.2f}")

# Check if matrix is invertible
det = np.linalg.det(A)
print(f"Determinant of A: {det:.6f}")

# Verify the solution
x_calculated = np.linalg.solve(A, b)
error = np.linalg.norm(x_calculated - x_known)
print(f"Solution error (L2 norm): {error:.2e}")
