# https://github.com/ellianak/lab10-EK-JT
# Partner 1: Elliana Kirby
# Partner 2: Joseph Torchio


"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)
def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a+b
def subtract(a, b):
    return a-b
def mul(a, b):
    return a*b
def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    else:
        return b/a
def logarithm(a, b):
    if b <= 1:
        raise ValueError
    return math.log(a, b)
def exp(a, b):
    return a**b
