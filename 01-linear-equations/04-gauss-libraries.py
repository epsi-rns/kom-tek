import numpy as np
import scipy.linalg
from scipy.sparse import csc_matrix
from scipy.sparse.linalg import spsolve
import time

# Example system: Ax = b
# 2x₁ + x₂ - x₃ = 8
# -3x₁ - x₂ + 2x₃ = -11  
# -2x₁ + x₂ + 2x₃ = -3

A = np.array([
    [2.0, 1.0, -1.0],
    [-3.0, -1.0, 2.0],
    [-2.0, 1.0, 2.0]
])

b = np.array([8.0, -11.0, -3.0])

print("SOLVING LINEAR SYSTEM Ax = b")
print("="*50)
print("System:")
print("2x₁ + x₂ - x₃ = 8")
print("-3x₁ - x₂ + 2x₃ = -11")
print("-2x₁ + x₂ + 2x₃ = -3")
print()

# Method 1: NumPy's linalg.solve (Most commonly used)
print("1. NUMPY linalg.solve() - MOST POPULAR")
print("-" * 40)
print("Usage: x = np.linalg.solve(A, b)")

start_time = time.time()
x1 = np.linalg.solve(A, b)
time1 = time.time() - start_time

print(f"Solution: {x1}")
print(f"Time: {time1:.6f} seconds")
print("✓ Fast, reliable, most commonly used")
print("✓ Uses optimized LAPACK routines")
print()

# Method 2: SciPy's linalg.solve (More options)
print("2. SCIPY linalg.solve() - MORE FEATURES")
print("-" * 40)
print("Usage: x = scipy.linalg.solve(A, b)")

start_time = time.time()
x2 = scipy.linalg.solve(A, b)
time2 = time.time() - start_time

print(f"Solution: {x2}")
print(f"Time: {time2:.6f} seconds")
print("✓ More options and algorithms")
print("✓ Can handle different matrix types")
print()

# Method 3: Matrix inversion (Not recommended for large systems)
print("3. MATRIX INVERSION - NOT RECOMMENDED")
print("-" * 40)
print("Usage: x = np.linalg.inv(A) @ b")

start_time = time.time()
x3 = np.linalg.inv(A) @ b
time3 = time.time() - start_time

print(f"Solution: {x3}")
print(f"Time: {time3:.6f} seconds")
print("⚠️  Slower and less numerically stable")
print("⚠️  Only use for small systems or when you need the inverse")
print()

# Method 4: Using @ operator with pseudoinverse (for over/under-determined systems)
print("4. PSEUDOINVERSE - FOR NON-SQUARE SYSTEMS")
print("-" * 40)
print("Usage: x = np.linalg.pinv(A) @ b")

start_time = time.time()
x4 = np.linalg.pinv(A) @ b
time4 = time.time() - start_time

print(f"Solution: {x4}")
print(f"Time: {time4:.6f} seconds")
print("✓ Works for non-square matrices")
print("✓ Finds least-squares solution")
print()

# Method 5: For sparse matrices
print("5. SPARSE MATRICES - FOR LARGE SYSTEMS")
print("-" * 40)
print("Usage: x = spsolve(A_sparse, b)")

A_sparse = csc_matrix(A)  # Convert to sparse format
start_time = time.time()
x5 = spsolve(A_sparse, b)
time5 = time.time() - start_time

print(f"Solution: {x5}")
print(f"Time: {time5:.6f} seconds")
print("✓ Excellent for large, sparse systems")
print("✓ Much faster when matrix has many zeros")
print()

# Verification
print("VERIFICATION - All methods should give same result:")
print("="*50)
solutions = [x1, x2, x3, x4, x5]
methods = ["NumPy solve", "SciPy solve", "Matrix inverse", "Pseudoinverse", "Sparse solve"]

for i, (method, solution) in enumerate(zip(methods, solutions)):
    error = np.linalg.norm(A @ solution - b)
    print(f"{method:<15}: Error = {error:.2e} {'✓' if error < 1e-10 else '✗'}")

print()

# PRACTICAL EXAMPLES FOR DIFFERENT SCENARIOS
print("WHEN TO USE EACH METHOD:")
print("="*50)

print("\n🎯 GENERAL PURPOSE (most common):")
print("   np.linalg.solve(A, b)")
print("   → Fast, reliable, works for most cases")

print("\n🎯 NEED SPECIAL OPTIONS:")
print("   scipy.linalg.solve(A, b, assume_a='pos')")  
print("   → When you know matrix properties (positive definite, etc.)")

print("\n🎯 LARGE SPARSE MATRICES:")
print("   from scipy.sparse.linalg import spsolve")
print("   spsolve(A_sparse, b)")
print("   → When your matrix has many zeros")

print("\n🎯 OVER/UNDER-DETERMINED SYSTEMS:")
print("   np.linalg.lstsq(A, b)")
print("   → When A is not square (more/fewer equations than unknowns)")

print("\n🎯 MULTIPLE RIGHT-HAND SIDES:")
print("   np.linalg.solve(A, B)  # B is a matrix")
print("   → Solve Ax₁=b₁, Ax₂=b₂, ... simultaneously")

# Example: Multiple right-hand sides
print("\n" + "="*50)
print("BONUS: MULTIPLE RIGHT-HAND SIDES")
print("-" * 30)

# Solve multiple systems at once: Ax₁=b₁, Ax₂=b₂
B = np.array([
    [8.0, 1.0],    # Two different b vectors
    [-11.0, 2.0],
    [-3.0, 3.0]
])

X = np.linalg.solve(A, B)  # Solve both at once!

print("Solving Ax₁ = b₁ and Ax₂ = b₂ simultaneously:")
print(f"x₁ = {X[:, 0]}")
print(f"x₂ = {X[:, 1]}")
print("✓ Much faster than solving separately!")

print("\n" + "="*50)
print("BOTTOM LINE:")
print("For 99% of cases, just use: np.linalg.solve(A, b)")
print("It's fast, reliable, and handles most situations perfectly!")
