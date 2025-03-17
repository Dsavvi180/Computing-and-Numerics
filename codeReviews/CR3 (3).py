import numpy as np

def midpoint(f, a, b, M):
    '''
    Returns the integral of a generic function f calculated by the midpoint rule over the interval [a,b] using M subintervals as instructed.
    '''
    I_approx = 0

    for i in range(M):
        # sub-area = height at midpoint * width of sub-interval
        I_approx += f(a + ((b-a)/M)*(i+0.5)) * (b-a)/M
    
    return I_approx
