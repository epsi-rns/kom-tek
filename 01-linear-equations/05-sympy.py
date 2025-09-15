import sympy as sp
from sympy import Matrix, pprint, symbols, Rational
import sympy.printing.pretty as pretty

def gauss_elimination_with_steps(A, b):
    """
    Perform Gaussian elimination with detailed step-by-step output using SymPy
    """
    print("GAUSSIAN ELIMINATION WITH SYMPY - STEP BY STEP")
    print("=" * 60)
    
    # Create augmented matrix [A|b]
    augmented = A.row_join(b)
    n = A.rows
    
    print("Initial augmented matrix [A|b]:")
    pprint(augmented, use_unicode=True)
    print()
    
    print("FORWARD ELIMINATION:")
    print("-" * 40)
    
    # Forward elimination
    for i in range(n):
        print(f"\nStep {i+1}: Working on column {i+1}")
        print("-" * 25)
        
        # Find pivot (in SymPy, we can work with exact arithmetic)
        pivot_row = i
        for k in range(i+1, n):
            if abs(augmented[k, i]) > abs(augmented[pivot_row, i]):
                pivot_row = k
        
        # Swap rows if needed
        if pivot_row != i:
            print(f"Swapping row {i+1} with row {pivot_row+1} for better pivot:")
            augmented = augmented.elementary_row_op('n<->m', row1=i, row2=pivot_row)
            pprint(augmented, use_unicode=True)
            print()
        
        # Check for zero pivot
        if augmented[i, i] == 0:
            print(f"Zero pivot encountered at position ({i+1}, {i+1})")
            continue
            
        print(f"Current pivot: {augmented[i, i]}")
        
        # Eliminate below pivot
        for k in range(i+1, n):
            if augmented[k, i] != 0:
                factor = augmented[k, i] / augmented[i, i]
                print(f"\nR{k+1} = R{k+1} - ({factor}) * R{i+1}")
                
                # Perform row operation
                augmented = augmented.elementary_row_op('n->n+km', 
                                                      row=k, k=-factor, row2=i)
                
                print("Result:")
                pprint(augmented, use_unicode=True)
    
    print("\n" + "=" * 60)
    print("UPPER TRIANGULAR FORM ACHIEVED!")
    print("Final augmented matrix:")
    pprint(augmented, use_unicode=True)
    
    return augmented

def back_substitution_with_steps(augmented_matrix):
    """
    Perform back substitution with step-by-step output
    """
    print("\n\nBACK SUBSTITUTION:")
    print("-" * 40)
    
    n = augmented_matrix.rows
    x = [0] * n
    
    # Create symbolic variables for display
    variables = [sp.Symbol(f'x_{i+1}') for i in range(n)]
    
    for i in range(n-1, -1, -1):
        print(f"\nSolving for x_{i+1}:")
        print("-" * 15)
        
        # Extract coefficients and constant
        coeffs = [augmented_matrix[i, j] for j in range(n)]
        constant = augmented_matrix[i, n]
        
        # Build equation string for display
        equation_parts = []
        for j in range(n):
            if coeffs[j] != 0:
                if j == 0:
                    equation_parts.append(f"{coeffs[j]}*x_{j+1}")
                else:
                    sign = "+" if coeffs[j] > 0 else "-"
                    equation_parts.append(f" {sign} {abs(coeffs[j])}*x_{j+1}")
        
        equation_str = "".join(equation_parts) + f" = {constant}"
        print(f"Equation: {equation_str}")
        
        # Calculate sum of known variables
        known_sum = sum(coeffs[j] * x[j] for j in range(i+1, n))
        
        # Show the substitution
        if any(x[j] != 0 for j in range(i+1, n)):
            substitution_parts = []
            for j in range(i+1, n):
                if coeffs[j] != 0:
                    substitution_parts.append(f"{coeffs[j]}*{x[j]}")
            
            if substitution_parts:
                known_str = " + ".join(substitution_parts)
                print(f"Substituting known values: {coeffs[i]}*x_{i+1} + {known_str} = {constant}")
                print(f"Known sum: {known_sum}")
        
        # Solve for x[i]
        x[i] = (constant - known_sum) / coeffs[i]
        print(f"x_{i+1} = ({constant} - ({known_sum})) / {coeffs[i]} = {x[i]}")
    
    return x

def solve_with_rref(A, b):
    """
    Alternative method using SymPy's built-in RREF (Reduced Row Echelon Form)
    """
    print("\n\nALTERNATIVE: USING SYMPY'S BUILT-IN RREF")
    print("=" * 50)
    
    # Create augmented matrix
    augmented = A.row_join(b)
    
    print("Original augmented matrix:")
    pprint(augmented, use_unicode=True)
    
    print("\nApplying rref() - this does Gauss-Jordan elimination:")
    reduced_matrix, pivot_cols = augmented.rref()
    
    print("Reduced Row Echelon Form:")
    pprint(reduced_matrix, use_unicode=True)
    
    print(f"Pivot columns: {pivot_cols}")
    
    # Extract solution
    n = A.rows
    solution = [reduced_matrix[i, n] for i in range(n)]
    
    return solution, reduced_matrix

# Example usage
if __name__ == "__main__":
    print("EXAMPLE 1: 3x3 System")
    print("=" * 30)
    print("System:")
    print("2x₁ + x₂ - x₃ = 8")
    print("-3x₁ - x₂ + 2x₃ = -11")
    print("-2x₁ + x₂ + 2x₃ = -3")
    print()
    
    # Define the system using exact fractions for cleaner output
    A1 = Matrix([
        [2, 1, -1],
        [-3, -1, 2],
        [-2, 1, 2]
    ])
    
    b1 = Matrix([8, -11, -3])
    
    # Method 1: Manual step-by-step Gaussian elimination
    upper_triangular = gauss_elimination_with_steps(A1, b1)
    solution1 = back_substitution_with_steps(upper_triangular)
    
    print(f"\nFINAL SOLUTION (Manual method):")
    for i, val in enumerate(solution1):
        print(f"x_{i+1} = {val}")
    
    # Method 2: Using SymPy's built-in RREF
    solution2, rref_matrix = solve_with_rref(A1, b1)
    
    print(f"\nFINAL SOLUTION (RREF method):")
    for i, val in enumerate(solution2):
        print(f"x_{i+1} = {val}")
    
    # Verification
    print("\nVERIFICATION:")
    print("-" * 20)
    result = A1 * Matrix(solution1)
    print("A * x =")
    pprint(result, use_unicode=True)
    print("\nShould equal b =")
    pprint(b1, use_unicode=True)
    print(f"\nMatch: {result == b1}")
    
    # Example 2: System with fractions
    print("\n\n" + "=" * 60)
    print("EXAMPLE 2: System with Fractions")
    print("=" * 30)
    
    A2 = Matrix([
        [Rational(1,2), Rational(1,3), Rational(1,4)],
        [Rational(1,3), Rational(1,4), Rational(1,5)],
        [Rational(1,4), Rational(1,5), Rational(1,6)]
    ])
    
    b2 = Matrix([1, 1, 1])
    
    print("Matrix A:")
    pprint(A2, use_unicode=True)
    print("\nVector b:")
    pprint(b2, use_unicode=True)
    
    # Solve using RREF for cleaner output with fractions
    solution_frac, _ = solve_with_rref(A2, b2)
    
    print(f"\nSOLUTION:")
    for i, val in enumerate(solution_frac):
        print(f"x_{i+1} = {val}")
    
    print("\nNOTE: SymPy keeps exact fractions - no rounding errors!")
    
    print("\n" + "=" * 60)
    print("SYMPY ADVANTAGES:")
    print("• Exact arithmetic (fractions, not decimals)")
    print("• Beautiful mathematical formatting")
    print("• Built-in RREF function")
    print("• Symbolic computation capabilities")
    print("• Perfect for educational purposes!")
