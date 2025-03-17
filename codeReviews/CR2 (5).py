import numpy as np

def polyfit_coeffs(x, y):
    '''
    Inputs
    ------
    * x: 4 dimentsional vector containing the x values of the known points (x_i)
    * y: 4 directional vector containing the corresponding y values (y_i)
    
    The function constructs a system of linear equations based on the four given polynomials, 
    and solves for the coefficients
    
    Outputs
    -------
    * a: 4 dimensional vector containing the computed coefficients (a_i)
    '''
    # defines an empty list which we can add items to
    P = []
    
    for x_i in x:
        row = [
            1 - x_i**3,     # p_0(x)
            x_i + x_i**2,   # p_1(x)
            x_i**2 - x_i,   # p_2(x)
            1 + x_i**3      # p_3(x)
        ]
        # each function p_i(x) is appended to the list using a for loop
        P.append(row)
        
    # convert the list to a numpy array
    P = np.array(P)
    
    # solve the linear system                    
    a = np.linalg.solve(P, y)
    
    return a

x = np.array([1.0, 2.0, 3.0, 4.0])
y = x ** 3

a = polyfit_coeffs(x, y)

print(f"{len(a.shape):d}")
print(f"{len(a):d}")
print(f"{a[0]:.4f}")
print(f"{abs(a[1]):.4f}")
print(f"{abs(a[2]):.4f}")
print(f"{a[3]:.4f}")