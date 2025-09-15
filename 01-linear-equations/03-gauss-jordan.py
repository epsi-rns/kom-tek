import numpy as np
from copy import deepcopy

def print_system(A, b, title=""):
    """Helper function to print the system nicely"""
    if title:
        print(f"\n{title}")
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
    print()

def gaussian_elimination(A, b):
    """Regular Gaussian Elimination - stops at upper triangular form"""
    print("GAUSSIAN ELIMINATION")
    print("="*50)
    
    n = len(A)
    A = deepcopy(A)
    b = deepcopy(b)
    
    print_system(A, b, "Initial system:")
    
    # Forward elimination only
    print("FORWARD ELIMINATION:")
    print("-" * 30)
    
    for i in range(n):
        print(f"\nStep {i+1}: Working on column {i+1}")
        
        # Partial pivoting
        max_row = i
        for k in range(i+1, n):
            if abs(A[k][i]) > abs(A[max_row][i]):
                max_row = k
        
        if max_row != i:
            A[i], A[max_row] = A[max_row], A[i]
            b[i], b[max_row] = b[max_row], b[i]
            print(f"  Swapped rows {i+1} and {max_row+1}")
        
        # Eliminate below pivot
        for k in range(i+1, n):
            if abs(A[k][i]) > 1e-10:
                factor = A[k][i] / A[i][i]
                print(f"  R{k+1} = R{k+1} - ({factor:.3f}) * R{i+1}")
                
                for j in range(i, n):
                    A[k][j] -= factor * A[i][j]
                b[k] -= factor * b[i]
        
        print_system(A, b, "  Current system:")
    
    print("UPPER TRIANGULAR FORM ACHIEVED!")
    print("Now need back substitution...")
    print_system(A, b, "Final upper triangular system:")
    
    # Back substitution
    print("BACK SUBSTITUTION:")
    print("-" * 20)
    
    x = [0.0] * n
    for i in range(n-1, -1, -1):
        x[i] = b[i]
        for j in range(i+1, n):
            x[i] -= A[i][j] * x[j]
        x[i] /= A[i][i]
        print(f"x{i+1} = {x[i]:.6f}")
    
    return x

def gauss_jordan_elimination(A, b):
    """Gauss-Jordan Elimination - goes to reduced row echelon form"""
    print("\n\nGAUSS-JORDAN ELIMINATION")
    print("="*50)
    
    n = len(A)
    A = deepcopy(A)
    b = deepcopy(b)
    
    print_system(A, b, "Initial system:")
    
    # Forward elimination
    print("FORWARD ELIMINATION:")
    print("-" * 30)
    
    for i in range(n):
        print(f"\nStep {i+1}: Working on column {i+1}")
        
        # Partial pivoting
        max_row = i
        for k in range(i+1, n):
            if abs(A[k][i]) > abs(A[max_row][i]):
                max_row = k
        
        if max_row != i:
            A[i], A[max_row] = A[max_row], A[i]
            b[i], b[max_row] = b[max_row], b[i]
            print(f"  Swapped rows {i+1} and {max_row+1}")
        
        # Scale pivot row to make pivot = 1
        if abs(A[i][i]) > 1e-10:
            pivot = A[i][i]
            print(f"  R{i+1} = R{i+1} / {pivot:.3f} (making pivot = 1)")
            for j in range(n):
                A[i][j] /= pivot
            b[i] /= pivot
        
        # Eliminate below pivot
        for k in range(i+1, n):
            if abs(A[k][i]) > 1e-10:
                factor = A[k][i]
                print(f"  R{k+1} = R{k+1} - ({factor:.3f}) * R{i+1}")
                
                for j in range(n):
                    A[k][j] -= factor * A[i][j]
                b[k] -= factor * b[i]
        
        print_system(A, b, "  Current system:")
    
    print("BACKWARD ELIMINATION (the extra step!):")
    print("-" * 40)
    
    # Backward elimination - this is what makes it Gauss-Jordan!
    for i in range(n-1, -1, -1):
        print(f"\nStep: Eliminate above pivot in column {i+1}")
        
        # Eliminate above pivot
        for k in range(i):
            if abs(A[k][i]) > 1e-10:
                factor = A[k][i]
                print(f"  R{k+1} = R{k+1} - ({factor:.3f}) * R{i+1}")
                
                for j in range(n):
                    A[k][j] -= factor * A[i][j]
                b[k] -= factor * b[i]
        
        print_system(A, b, "  Current system:")
    
    print("REDUCED ROW ECHELON FORM ACHIEVED!")
    print("Solution appears directly in the constants column!")
    
    # The solution is now directly in vector b
    return list(b)

def compare_methods():
    """Compare both methods side by side"""
    # Example system:
    # 2x₁ + x₂ - x₃ = 8
    # -3x₁ - x₂ + 2x₃ = -11
    # -2x₁ + x₂ + 2x₃ = -3
    
    A = [
        [2.0, 1.0, -1.0],
        [-3.0, -1.0, 2.0],
        [-2.0, 1.0, 2.0]
    ]
    b = [8.0, -11.0, -3.0]
    
    print("SOLVING THE SAME SYSTEM WITH BOTH METHODS:")
    print("System:")
    print("2x₁ + x₂ - x₃ = 8")
    print("-3x₁ - x₂ + 2x₃ = -11")
    print("-2x₁ + x₂ + 2x₃ = -3")
    print("\n" + "="*70)
    
    # Method 1: Regular Gaussian Elimination
    solution1 = gaussian_elimination(A, b)
    
    # Method 2: Gauss-Jordan Elimination  
    solution2 = gauss_jordan_elimination(A, b)
    
    print("\n" + "="*70)
    print("COMPARISON OF RESULTS:")
    print("-" * 30)
    print(f"{'Variable':<10} {'Gaussian':<15} {'Gauss-Jordan':<15} {'Match?'}")
    print("-" * 50)
    
    for i in range(len(solution1)):
        match = "✓" if abs(solution1[i] - solution2[i]) < 1e-6 else "✗"
        print(f"x{i+1:<9} {solution1[i]:<15.6f} {solution2[i]:<15.6f} {match}")
    
    print("\nKEY DIFFERENCES:")
    print("• Gaussian: Forward elimination → Back substitution")
    print("• Gauss-Jordan: Forward elimination → Backward elimination (no back substitution needed)")
    print("• Gauss-Jordan produces identity matrix directly")
    print("• Both methods give the same solution!")

if __name__ == "__main__":
    compare_methods()
