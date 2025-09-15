import numpy as np
import random
from fractions import Fraction

class LinearSystemGenerator:
    """Generate random linear systems with known solutions for testing"""
    
    def __init__(self, seed=None):
        """Initialize with optional seed for reproducible results"""
        if seed is not None:
            random.seed(seed)
            np.random.seed(seed)
    
    def generate_basic_system(self, size=3, coeff_range=(-5, 5), solution_range=(-3, 3)):
        """
        Method 1: Start with known solution, generate random coefficients
        Most reliable method - always produces solvable system
        """
        print(f"GENERATING {size}x{size} SYSTEM - METHOD 1")
        print("=" * 50)
        
        # Step 1: Generate known solution
        solution = [random.randint(*solution_range) for _ in range(size)]
        print(f"Target solution: x = {solution}")
        
        # Step 2: Generate random coefficient matrix
        # Avoid zeros on diagonal for stability
        A = np.zeros((size, size), dtype=int)
        for i in range(size):
            for j in range(size):
                if i == j:
                    # Diagonal elements: avoid zero
                    A[i, j] = random.choice([x for x in range(*coeff_range) if x != 0])
                else:
                    A[i, j] = random.randint(*coeff_range)
        
        print(f"Random coefficient matrix A:")
        self._print_matrix(A)
        
        # Step 3: Calculate b = A * x
        b = A @ solution
        
        print(f"Calculated b = A * x:")
        print(f"b = {b.tolist()}")
        
        return A, b, solution
    
    def generate_row_by_row(self, size=3, coeff_range=(-5, 5), solution_range=(-3, 3)):
        """
        Method 2: Build each equation row by row
        Good for understanding the process
        """
        print(f"GENERATING {size}x{size} SYSTEM - METHOD 2 (Row by Row)")
        print("=" * 60)
        
        # Step 1: Choose solution
        solution = [random.randint(*solution_range) for _ in range(size)]
        print(f"Target solution: x = {solution}")
        print()
        
        A = []
        b = []
        
        # Step 2: Build each equation
        for i in range(size):
            print(f"Building equation {i+1}:")
            
            # Generate random coefficients for this row
            row = [random.randint(*coeff_range) for _ in range(size)]
            
            # Calculate right-hand side
            rhs = sum(coeff * sol_val for coeff, sol_val in zip(row, solution))
            
            # Show the equation being built
            equation_parts = []
            for j, coeff in enumerate(row):
                if j == 0:
                    equation_parts.append(f"{coeff}x{j+1}")
                else:
                    sign = "+" if coeff >= 0 else "-"
                    equation_parts.append(f" {sign} {abs(coeff)}x{j+1}")
            
            equation_str = "".join(equation_parts) + f" = {rhs}"
            print(f"  {equation_str}")
            
            # Show calculation
            calc_parts = [f"{coeff}*{sol_val}" for coeff, sol_val in zip(row, solution)]
            calc_str = " + ".join(calc_parts) + f" = {rhs}"
            print(f"  Check: {calc_str}")
            print()
            
            A.append(row)
            b.append(rhs)
        
        return np.array(A), np.array(b), solution
    
    def generate_with_operations(self, size=3, solution_range=(-3, 3), num_operations=None):
        """
        Method 3: Start with identity matrix, apply random row operations
        Most pedagogical - shows how systems can be transformed
        """
        print(f"GENERATING {size}x{size} SYSTEM - METHOD 3 (Row Operations)")
        print("=" * 65)
        
        if num_operations is None:
            num_operations = size * 2  # Default number of operations
        
        # Step 1: Start with solution
        solution = [random.randint(*solution_range) for _ in range(size)]
        print(f"Target solution: x = {solution}")
        
        # Step 2: Start with identity matrix and solution as b
        A = np.eye(size, dtype=float)
        b = np.array(solution, dtype=float)
        
        print("\nStarting with identity system:")
        self._print_system(A, b)
        
        # Step 3: Apply random row operations
        print(f"\nApplying {num_operations} random row operations:")
        print("-" * 40)
        
        for op in range(num_operations):
            operation = random.choice(['swap', 'scale', 'add'])
            
            if operation == 'swap' and size > 1:
                # Swap two rows
                i, j = random.sample(range(size), 2)
                A[[i, j]] = A[[j, i]]
                b[[i, j]] = b[[j, i]]
                print(f"Op {op+1}: Swap rows {i+1} and {j+1}")
                
            elif operation == 'scale':
                # Scale a row by non-zero constant
                i = random.randint(0, size-1)
                factor = random.choice([-3, -2, 2, 3, 4])  # Avoid 1, -1, 0
                A[i] *= factor
                b[i] *= factor
                print(f"Op {op+1}: Scale row {i+1} by {factor}")
                
            else:  # add
                # Add multiple of one row to another
                i, j = random.sample(range(size), 2)
                factor = random.randint(-3, 3)
                if factor == 0:
                    factor = 1
                A[i] += factor * A[j]
                b[i] += factor * b[j]
                print(f"Op {op+1}: R{i+1} = R{i+1} + ({factor}) * R{j+1}")
        
        print("\nFinal system after row operations:")
        self._print_system(A, b)
        
        # Convert back to integers if possible
        A_int, b_int = self._try_convert_to_int(A, b)
        
        return A_int, b_int, solution
    
    def generate_special_cases(self, case_type='easy'):
        """Generate special types of systems for different learning objectives"""
        
        if case_type == 'easy':
            # Small integers, simple solution
            return self.generate_basic_system(size=2, coeff_range=(-3, 3), solution_range=(-2, 2))
        
        elif case_type == 'medium':
            # Larger coefficients, 3x3 system
            return self.generate_basic_system(size=3, coeff_range=(-8, 8), solution_range=(-5, 5))
        
        elif case_type == 'hard':
            # 4x4 system with larger range
            return self.generate_basic_system(size=4, coeff_range=(-10, 10), solution_range=(-7, 7))
        
        elif case_type == 'fractions':
            # Generate system with fractional solution
            A, b, _ = self.generate_basic_system(size=3, coeff_range=(-5, 5), solution_range=(-3, 3))
            # Modify to create fractional solutions
            A[0] = [2, 1, 1]  # Force some specific structure
            solution = [Fraction(1, 2), Fraction(-1, 3), Fraction(2, 3)]
            b = [sum(A[i][j] * float(solution[j]) for j in range(3)) for i in range(3)]
            return A, b, [float(s) for s in solution]
        
        elif case_type == 'zero_solution':
            # One or more variables equal zero
            solution = [0, random.randint(1, 3), random.randint(-2, 2)]
            A = np.random.randint(-5, 6, (3, 3))
            # Ensure no zero diagonal
            for i in range(3):
                if A[i, i] == 0:
                    A[i, i] = random.choice([-1, 1])
            b = A @ solution
            return A, b, solution
    
    def _print_matrix(self, matrix):
        """Helper to print matrix nicely"""
        for row in matrix:
            print(f"  {row}")
        print()
    
    def _print_system(self, A, b):
        """Helper to print system Ax = b nicely"""
        size = len(A)
        for i in range(size):
            equation_parts = []
            for j in range(size):
                coeff = A[i, j]
                if j == 0:
                    equation_parts.append(f"{coeff:6.1f}x{j+1}")
                else:
                    sign = "+" if coeff >= 0 else "-"
                    equation_parts.append(f" {sign} {abs(coeff):4.1f}x{j+1}")
            equation_str = "".join(equation_parts) + f" = {b[i]:6.1f}"
            print(f"  {equation_str}")
        print()
    
    def _try_convert_to_int(self, A, b):
        """Try to convert float arrays back to integers if possible"""
        try:
            A_int = A.astype(int)
            b_int = b.astype(int)
            # Check if conversion was exact
            if np.allclose(A, A_int) and np.allclose(b, b_int):
                return A_int, b_int
        except:
            pass
        return A, b
    
    def verify_solution(self, A, b, solution):
        """Verify that the generated solution is correct"""
        print("VERIFICATION:")
        print("-" * 20)
        computed_b = A @ solution
        print(f"A * solution = {computed_b}")
        print(f"Original b   = {b}")
        print(f"Match: {np.allclose(computed_b, b)}")
        if not np.allclose(computed_b, b):
            print("⚠️  WARNING: Solution doesn't match!")
        else:
            print("✓ Solution verified!")

# Example usage and demonstration
if __name__ == "__main__":
    generator = LinearSystemGenerator(seed=42)  # For reproducible examples
    
    print("LINEAR SYSTEM CASE GENERATOR DEMO")
    print("=" * 70)
    
    # Example 1: Basic method
    A1, b1, sol1 = generator.generate_basic_system()
    generator.verify_solution(A1, b1, sol1)
    
    print("\n" + "=" * 70)
    
    # Example 2: Row by row method
    A2, b2, sol2 = generator.generate_row_by_row()
    generator.verify_solution(A2, b2, sol2)
    
    print("\n" + "=" * 70)
    
    # Example 3: Row operations method
    A3, b3, sol3 = generator.generate_with_operations()
    generator.verify_solution(A3, b3, sol3)
    
    print("\n" + "=" * 70)
    
    # Example 4: Special cases
    print("SPECIAL CASE EXAMPLES:")
    print("-" * 30)
    
    cases = ['easy', 'medium', 'zero_solution']
    for case in cases:
        print(f"\n{case.upper()} case:")
        A, b, sol = generator.generate_special_cases(case)
        print(f"Solution: {sol}")
        generator._print_system(A, b)
    
    print("=" * 70)
    print("USAGE EXAMPLES:")
    print("• Use for testing your Gaussian elimination implementation")
    print("• Generate homework problems with known answers")
    print("• Create progressively harder examples for learning")
    print("• Verify your solver works correctly")
