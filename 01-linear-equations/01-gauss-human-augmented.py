import numpy as np

def gauss_eliminate(A, b):
    """
    Solves the system A*x = b using Gaussian Elimination with Partial Pivoting.
    
    Args:
        A: A square numpy array (the coefficient matrix).
        b: A numpy vector (the constant terms).
    
    Returns:
        x: The solution vector.
    """
    # Form the augmented matrix
    n = len(b)
    aug = np.hstack((A.astype(float), b.reshape(-1, 1).astype(float))) 
    print("Initial Augmented Matrix:")
    print(aug)
    print("-" * 40)

    # Forward Elimination with Partial Pivoting
    for i in range(n):
        # Partial Pivoting: Find the row with the largest element in column i
        max_row = i
        for k in range(i+1, n):
            if abs(aug[k, i]) > abs(aug[max_row, i]):
                max_row = k
        # Swap the current row with the max row
        aug[[i, max_row]] = aug[[max_row, i]]
        print(f"After pivoting for column {i}:")
        print(aug)

        # Check if the pivot is zero (matrix is singular)
        if abs(aug[i, i]) < 1e-10: # Using a small tolerance for floating-point
            raise ValueError("Matrix is singular or nearly singular. No unique solution.")

        # Eliminate all entries below the pivot
        for k in range(i+1, n):
            # Calculate the multiplier
            multiplier = aug[k, i] / aug[i, i]
            # Subtract multiplier * pivot row from current row
            aug[k, i:] -= multiplier * aug[i, i:]
        print(f"After elimination for column {i}:")
        print(aug)
        print("-" * 40)

    # Back Substitution
    x = np.zeros(n)
    for i in range(n-1, -1, -1): # Start from the last row
        # Start with the value in the right-most column (the constant 'b')
        x[i] = aug[i, -1]
        # Subtract the sum of (known variables * their coefficients)
        for j in range(i+1, n):
            x[i] -= aug[i, j] * x[j]
        # Solve for the current variable: x_i = value / coefficient_of_x_i
        x[i] /= aug[i, i]
    
    return x

# --- Example Usage ---
# Let's use the same system from our previous step-by-step walkthrough:
# 2x + y - z = 8
# -3x - y + 2z = -11
# -2x + y + 2z = -3

# Define the matrix A and vector b
A = np.array([
    [2, 1, -1],
    [-3, -1, 2],
    [-2, 1, 2]
])
b = np.array([8, -11, -3])

print("Solving the system:")
print("2x + y - z = 8")
print("-3x - y + 2z = -11")
print("-2x + y + 2z = -3\n")

# Solve using our function
try:
    x = gauss_eliminate(A, b)
    print(f"\nSolution found:")
    print(f"x = {x[0]:.2f}")
    print(f"y = {x[1]:.2f}")
    print(f"z = {x[2]:.2f}")

    # Verify the solution by computing A*x
    print("\nVerification (A * x should equal b):")
    print("A * x =", np.dot(A, x))
    print("b =    ", b)

except ValueError as e:
    print(e)
