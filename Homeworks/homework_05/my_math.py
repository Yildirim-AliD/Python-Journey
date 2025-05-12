# my_math.py

import math

def square_root(x):
    return x ** 0.5

def power(base, exp):
    return base ** exp

def logarithm(x, base=math.e):
    return math.log(x, base)

def sine(degrees):
    return math.sin(math.radians(degrees))

def cosine(degrees):
    return math.cos(math.radians(degrees))

def tangent(degrees):
    return math.tan(math.radians(degrees))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n+1):
        result *= i
    return result
