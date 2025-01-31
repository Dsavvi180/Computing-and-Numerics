from typing import List,Tuple, TypeVar
from decimal import Decimal
from fractions import Fraction
from enum import Enum 
from abc import ABC, abstractmethod

# Polynomial coefficients
a0 = 1
a1 = -2
a2 = 4.6
a3 = 0.2
# Point at which we evaluate the derivative
x0 = 3.1

coeff = [a0,a1,a2,a3] 

T = TypeVar('T', float, Decimal, Fraction)

class polynomial:

    def __init__(self, coefficients:List, x_term:T):
        self.ceofficients = coefficients
        self.x_term = x_term
        self.value = self.construct_polynomial(self.ceofficients, self.x_term)
        self.derivative = self.calculate_p_prime(self.ceofficients, self.x_term)
        self.x_term_type = type(x_term)

    def construct_polynomial(self, coefficients:List, x_term: T) -> T: #use type fraction.Fraction or decimal.Decimal for more precise arithmetics
        x_terms_power = [i for i in range(len(coefficients))] #instantiate with zero as first element
        terms = list(zip(coefficients,x_terms_power))
        p=0
        for coefficient, power in terms:
            p += coefficient*x_term**power
        return p

    def calculate_p_prime(self, coefficients:List, x_term: T) -> T:
        x_terms_power = [i for i in range(len(coefficients))] #instantiate with zero as first element
        terms = list(zip(coefficients,x_terms_power))
        p=0
        for coefficient, power in terms:
            p += power*coefficient*x_term**(power-1)
        return p
    


new_polynomial = polynomial(coeff,x0)

p_prime = new_polynomial.derivative
# This will be True if the code is correct
print(p_prime == 32.286)
