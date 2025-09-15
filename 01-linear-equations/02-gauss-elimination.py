import numpy as np
from copy import deepcopy

def gaussian_elimination_verbose(A, b):
    """
    Solve Ax = b using Gaussian elimination without augmented matrix.
    Shows step-by-step process.
    
    Args:
        A: coefficient matrix (n x n)
        b: constants vector (n x 1)
    
    Returns:
        x: solution vector
    """
    n = len(A)
    A = deepcopy(A)  # Don't modify original matrices
    b = deepcopy(b)
    
    print("Initial system:")
    print_system(A, b)
    print("\n" + "="*50)
    
    # Forward elimination
    print("\nFORWARD ELIMINATION:")
    print("-" * 30)
    
    for i in range(n):
        print(f"\nStep {i+1}: Eliminate column {i+1}")
        
        # Find pivot (largest element in column i, row i and below)
        max_row = i
        for k in range(i+1, n):
            if abs(A[k][i]) > abs(A[max_row][i]):
                max_row = k
        
        # Swap rows if needed
        if max_row != i:
            A[i], A[max_row] = A[max_row], A[i]
            b[i], b[max_row] = b[max_row], b[i]
            print(f"  Swapped rows {i+1} and {max_row+1}")
            print_system(A, b)
        
        # Check for zero pivot
        if abs(A[i][i]) < 1e-10:
            raise ValueError(f"Zero pivot encountered at position ({i}, {i})")
        
        # Eliminate below pivot
        for k in range(i+1, n):
            if A[k][i] != 0:
                factor = A[k][i] / A[i][i]
                print(f"  R{k+1} = R{k+1} - ({factor:.3f}) * R{i+1}")
                
                # Apply to matrix A
                for j in range(i, n):
                    A[k][j] -= factor * A[i][j]
                
                # Apply to vector b
                b[k] -= factor * b[i]
        
        print("  Result:")
        print_system(A, b)
    
    print("\n" + "="*50)
    print("\nBACK SUBSTITUTION:")
    print("-" * 30)
    
    # Back substitution
    x = [0.0] * n
    
    for i in range(n-1, -1, -1):
        print(f"\nSolving for x{i+1}:")
        
        # Calculate sum of known variables
        sum_ax = 0
        equation_parts = []
        
        for j in range(i+1, n):
            if A[i][j] != 0:
                sum_ax += A[i][j] * x[j]
                equation_parts.append(f"({A[i][j]:.3f})*{x[j]:.3f}")
        
        # Solve for x[i]
        x[i] = (b[i] - sum_ax) / A[i][i]
        
        # Show the equation
        equation_str = f"{A[i][i]:.3f} * x{i+1}"
        if equation_parts:
            equation_str += " + " + " + ".join(equation_parts)
        equation_str += f" = {b[i]:.3f}"
        
        print(f"  {equation_str}")
        print(f"  x{i+1} = ({b[i]:.3f} - {sum_ax:.3f}) / {A[i][i]:.3f} = {x[i]:.6f}")
    
    return x

def print_system(A, b):
    """Helper function to print the system of equations nicely"""
    n = len(A)
    for i in range(n):
        equation = ""
        for j in range(n):
            coeff = A[i][j]
            if j == 0:
                equation += f"{coeff:8.3f}*x{j+1}"
            else:
                sign = "+" if coeff >= 0 else "-"
                equation += f" {sign} {abs(coeff):6.3f}*x{j+1}"
        equation += f" = {b[i]:8.3f}"
        print(f"  {equation}")

def gaussian_elimination_simple(A, b):
    """
    Simple version without verbose output
    """
    n = len(A)
    A = deepcopy(A)
    b = deepcopy(b)
    
    # Forward elimination
    for i in range(n):
        # Partial pivoting
        max_row = i
        for k in range(i+1, n):
            if abs(A[k][i]) > abs(A[max_row][i]):
                max_row = k
        A[i], A[max_row] = A[max_row], A[i]
        b[i], b[max_row] = b[max_row], b[i]
        
        # Eliminate
        for k in range(i+1, n):
            if A[k][i] != 0:
                factor = A[k][i] / A[i][i]
                for j in range(i, n):
                    A[k][j] -= factor * A[i][j]
                b[k] -= factor * b[i]
    
    # Back substitution
    x = [0.0] * n
    for i in range(n-1, -1, -1):
        x[i] = b[i]
        for j in range(i+1, n):
            x[i] -= A[i][j] * x[j]
        x[i] /= A[i][i]
    
    return x

# Example usage
if __name__ == "__main__":
    # Example 1: Simple 3x3 system
    print("EXAMPLE 1: 3x3 System")
    print("=" * 60)
    
    A1 = [
        [2.0, 1.0, -1.0],
        [-3.0, -1.0, 2.0],
        [-2.0, 1.0, 2.0]
    ]
    b1 = [8.0, -11.0, -3.0]
    
    print("Solving system:")
    print("2x₁ + x₂ - x₃ = 8")
    print("-3x₁ - x₂ + 2x₃ = -11") 
    print("-2x₁ + x₂ + 2x₃ = -3")
    print()
    
    solution1 = gaussian_elimination_verbose(A1, b1)
    
    print(f"\nFINAL SOLUTION:")
    for i, val in enumerate(solution1):
        print(f"x{i+1} = {val:.6f}")
    
    # Verification
    print(f"\nVerification (Ax = b):")
    A1_orig = [[2.0, 1.0, -1.0], [-3.0, -1.0, 2.0], [-2.0, 1.0, 2.0]]
    for i in range(len(A1_orig)):
        result = sum(A1_orig[i][j] * solution1[j] for j in range(len(solution1)))
        print(f"Row {i+1}: {result:.6f} (should be {b1[i]})")
    
    print("\n" + "="*60)
    print("\nEXAMPLE 2: Another system (simple output)")
    print("-" * 40)
    
    A2 = [
        [1.0, 2.0, 3.0],
        [2.0, -1.0, 1.0],
        [3.0, 0.0, -1.0]
    ]
    b2 = [9.0, 8.0, 3.0]
    
    solution2 = gaussian_elimination_simple(A2, b2)
    print("Solution:", [f"x{i+1} = {val:.6f}" for i, val in enumerate(solution2)])
