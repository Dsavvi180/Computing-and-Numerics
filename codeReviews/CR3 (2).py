import numpy as np

def midpoint(f, a, b, M):
    h = (b - a) / M  # Compute step size
    midpoints = np.linspace(a + h/2, b - h/2, M)  # Generate midpoints of subintervals
    integral = h * np.sum(f(midpoints))  # Approximate the integral using the midpoint rule
    return integral