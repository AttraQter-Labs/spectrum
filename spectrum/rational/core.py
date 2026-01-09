from fractions import Fraction

def rational_divide(n, d):
    if d == 0:
        raise ZeroDivisionError
    return Fraction(n, d)
