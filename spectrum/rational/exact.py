"""Exact rational arithmetic utilities for deterministic computations."""

from fractions import Fraction


def rational_divide(n: int, d: int) -> Fraction:
    """Divide two integers exactly using rational arithmetic.
    
    Provides exact division without floating-point rounding errors.
    Returns a Fraction representing the exact ratio n/d.
    
    Args:
        n: Numerator (integer)
        d: Denominator (integer, must be non-zero)
        
    Returns:
        Fraction representing n/d exactly
        
    Raises:
        ZeroDivisionError: If d is zero
        
    Example:
        >>> rational_divide(1, 3)
        Fraction(1, 3)
        >>> rational_divide(2, 4)
        Fraction(1, 2)  # Automatically reduced
    """
    if d == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return Fraction(n, d)
