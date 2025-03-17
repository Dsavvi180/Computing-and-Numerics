import numpy as np

def polyfit_coeffs(x, y):
    
    # Constructing the system matrix
    A = np.array([
        [1 - x[i]**3, x[i] + x[i]**2, x[i]**2 - x[i], 1 + x[i]**3]
        for i in range(4)
        ])

    # Solving the linear system A * a = y
    a = np.linalg.solve(A, y)
    
    return a 
    
# Test case
x = np.array([1.0, 2.0, 3.0, 4.0])
y = x ** 3

a = polyfit_coeffs(x, y)

print(f"{len(a.shape):d}")
print(f"{len(a):d}")
print(f"{a[0]:.4f}")
print(f"{abs(a[1]):.4f}")
print(f"{abs(a[2]):.4f}")
print(f"{a[3]:.4f}")