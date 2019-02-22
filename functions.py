"""
Definiton of useful functions
"""

def summation(start, stop, function):
    output = 0
    for i in range(start, stop + 1):
        output += function(i)
    return output

def product(start, stop, function):
    output = 1
    for i in range(start, stop + 1):
        output *= function(i)
    return output

def factorial(n):
    if n == 0:
        return 1
    return product(1, n, lambda x: x)

def C(n, r):
    n_factorial = factorial(n)
    r_factorial = factorial(r)
    n_min_r_factorial = factorial(n - r)
    return n_factorial / (r_factorial * n_min_r_factorial)

def n_choose_r(n, r):
    return C(n, r)

def P(n, r):
    n_factorial = factorial(n)
    n_min_r_factorial = factorial(n -r)
    return n_factorial / n_min_r_factorial
