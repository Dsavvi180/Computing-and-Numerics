from typing import List

# Function type signature restricting argument and output types


def every_nth(n: int, p: int) -> List[int]:
    """
    Calculates every nth integer between p/2 and p, starting with p/2.

    Args:
         n (int): A positive integer, must be less than or equal to p/2.
         p (int): A positve even integer.

    Returns: 
         List[int]: List of integers of the calculated values.
    """
    if n <= 0 or p <= 0 or n > p/2 or p % 2 != 0:
        # Raises a value error if the arguments do not match the specified criteria
        raise ValueError("Invalid values provided.")
        return
    return [i for i in range(int(p/2), int(p+1), int(n))]
