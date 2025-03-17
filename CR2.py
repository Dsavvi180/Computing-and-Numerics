import numpy as np
import typing
import sympy as sp

# Creates symbol objects for each coefficient
a0, a1, a2, a3 = sp.symbols('a0 a1 a2 a3')


def p0(x):
    return 1-x ** 3


def p1(x):
    return x+x ** 2


def p2(x):
    return x ** 2-x


def p3(x):
    return 1+x ** 3


def p(x):
    return a0*p0(x)+a1*p1(x)+a2*p2(x)+a3*p3(x)


def polyfit_coeffs(x: np.ndarray, y: np.ndarray) -> np.array:
    """
    Solves for the coefficients of a polynomial by fitting the polynomial to (X_i,Y_i) points, for i is an element of {0,...,3}, 
    where X_i is the element in the ith index of the x parameter and analogously for Y_i.

    Under the hood, the SymPy library is used, where SymPy equations are constructed of the form p(X_i) = Y_i and are solved by SymPy using numerical methods.

    Args:
         x (np.array(float[4])): A numpy vector holding only float data types of length 4. 
         y (np.array(float[4])): A numpy vector holding only float data types of length 4. 

    Returns:
         a (np.array(float[4])): A numpy vector holding only float data types of length 4. 

    """

    if len(x)+len(y) != 8 or x.dtype != float or y.dtype != float:
        raise ValueError(
            "Each input parameter must be a numpy vector of length 4")

    # Dynamically creates a system of SymPy equations with x,y inputs, using list comprehension, from the structure [(x,y)] returned by the zip function
    equations = (sp.Eq(p(x), y) for x, y in zip(x, y))
    coeffs = (a0, a1, a2, a3)
    a = np.array([float(i) for i in sp.solve(equations, coeffs).values()])

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