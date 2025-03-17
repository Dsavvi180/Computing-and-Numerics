import numpy as np


def midpoint(f, a, b, M):
    """
    Returns the integral of a generic function f calculated by the midpoint rule over the interval [a,b] using M subintervals as instructed.

    Args:
         f (a function): A mathematical function
         a (float):      A number
         b (float):      A number
         M (integer):    A positive integer

    Returns:
        A floating point number

    """
    direction = -1 if a > b else 1  # Directional encoding indicating whether the interval is increasing or decreasing
    width = abs(a-b)/M
    left_bound = a+width/2 if a < b else a-width/2
    right_bound = b+width/2 if a < b else b-width/2
    # Takes the sum of the interval areas, which are calculated by multiplying the interval width with the height of the interval's midpoint.
    return sum([direction*width*f(point) for point in np.linspace(left_bound, right_bound, num=M, endpoint=False)])
