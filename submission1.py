# Question 1
def every_nth(n, p):
    if (n <= 0 and p <= 0) or (n > p/2) or (p % 2 != 0):
        raise ValueError("Invalid values provided.")
        return
    return [i for i in range(int(p/2), int(p+1), int(n))]


def sequence_element(n):
    if n < 0:
        raise ValueError("Invalid values provided.")
    sequence = [1, 2] + [None for i in range(2, n+1)]
    current = 2
    while current <= n:
        previous = current - 1
        second_previous = current-2
        if sequence[previous] % 2 == 0:
            sequence[current] = 3*sequence[second_previous]
        else:
            sequence[current] = 2*sequence[previous]-sequence[second_previous]
        current += 1
    return sequence[n]


def quotients(x):
    dividend = round(x)
    divisors = [2,5,7,11]
    quotients = []
    for divisor in divisors:
        quotients.append(dividend//divisor)
    return quotients

def sum_reciprocals(n):
    return float(round(sum([1/i for i in range(1,n+1)]),5))


