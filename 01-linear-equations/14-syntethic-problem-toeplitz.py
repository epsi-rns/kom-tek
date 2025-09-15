import numpy as np
from scipy.linalg import toeplitz, circulant

def generate_linear_system_builtin(n, matrix_type='toeplitz', value_range=(-10, 10)):
    """
    Generates a linear system using built-in test matrix generators.
    """
    min_val, max_val = value_range
    x_known = np.random.randint(min_val, max_val + 1, size=n)
    
    if matrix_type == 'toeplitz':
        # Toeplitz matrices are often well-conditioned
        c = np.random.randint(-5, 6, size=n)
        r = np.random.randint(-5, 6, size=n)
        r[0] = c[0]  # First element must be the same
        A = toeplitz(c, r)
        
    elif matrix_type == 'circulant':
        # Circulant matrices have known properties
        c = np.random.randint(-5, 6, size=n)
        A = circulant(c)
        
    elif matrix_type == 'random_orthogonal':
        # Generate a random orthogonal matrix (perfect condition number = 1)
        A, _ = linalg.qr(np.random.randn(n, n))
        
    else:
        raise ValueError("Unknown matrix type")
    
    # Make sure we have an invertible matrix
    if np.linalg.det(A) == 0:
        # Add a small identity matrix to ensure invertibility
        A = A + 0.1 * np.eye(n)
    
    b = A @ x_known
    return A, b, x_known

# Example using built-in matrices
print("Using built-in Toeplitz matrix:")
A_toep, b_toep, x_known_toep = generate_linear_system_builtin(3, 'toeplitz')
print("A =\n", A_toep)
print("b =", b_toep)
print("x_known =", x_known_toep)
