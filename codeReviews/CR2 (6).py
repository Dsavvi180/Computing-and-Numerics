import numpy as np

def polyfit_coeffs(x, y):
    '''
    Returns the coefficients a_i.
    '''
    
    # Establish matrix A where each row is p(xi).
    A = np.array([[1-x[0]**3, x[0] + x[0]**2, x[0]**2 - x[0], 1 + x[0]**3],
                [1-x[1]**3, x[1] + x[1]**2, x[1]**2 - x[1], 1 + x[1]**3],
                [1-x[2]**3, x[2] + x[2]**2, x[2]**2 - x[2], 1 + x[2]**3],
                [1-x[3]**3, x[3] + x[3]**2, x[3]**2 - x[3], 1 + x[3]**3]], dtype = float)
        
    # Establish vector b which is the solution vector y.
    b = np.array(y, dtype = float)

    # Thus now the system of equations p(xi)=yi can be represented by Ax=b where x is a vector of the coefficients ai. This can be solved to find the coefficient vector ai.
    return np.linalg.solve(A, b)

x = np.array([1.0, 2.0, 3.0, 4.0])
y = x ** 3

a = polyfit_coeffs(x, y)

print(f"{len(a.shape):d}")
print(f"{len(a):d}")
print(f"{a[0]:.4f}")
print(f"{abs(a[1]):.4f}")
print(f"{abs(a[2]):.4f}")
print(f"{a[3]:.4f}")