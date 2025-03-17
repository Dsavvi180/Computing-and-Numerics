import numpy as np

def midpoint(f, a, b, M):
    '''
    Returns the integral of a generic function f calculated by the midpoint rule over the interval [a,b] using M subintervals as instructed.
    '''
# define the width of each interval as h.
    h = (b-a)/(M)
# calculate the midpoint approx for the integral as the sum of the width of each interval times by the height of the midpoint of that interval.
    Iapprox = 0
    for i in range(M):
        Iapprox += (h*f(a-h/2+h*(i+1)))
    return Iapprox
