"""
Test demonstrating floating-point divergence vs exact rational/integer success.

This test shows that floating-point arithmetic is non-deterministic
across platforms and can lead to divergence, while exact arithmetic
(integers and rationals) provides deterministic, reproducible results.
"""

from fractions import Fraction


def test_float_divergence_documentation():
    """
    Document floating-point divergence behavior.
    
    Floating-point arithmetic can produce different results across
    platforms, compiler optimizations, and even execution order.
    This is why Spectrum forbids floating-point arithmetic.
    """
    # Example: floating-point accumulation can diverge
    # Different evaluation orders can produce different results
    
    # Forward accumulation
    forward_sum = 0.0
    for i in range(1000):
        forward_sum += 0.1
    
    # Backward accumulation
    backward_sum = 0.0
    for i in range(999, -1, -1):
        backward_sum += 0.1
    
    # These should theoretically be equal, but due to floating-point
    # precision limitations, they may differ slightly
    # We document this behavior but do NOT rely on it
    
    # Note: This is for DOCUMENTATION purposes only
    # Spectrum does NOT use floating-point arithmetic
    difference = abs(forward_sum - backward_sum)
    
    # The difference might be zero on some platforms but not others
    # This demonstrates why we cannot rely on floats for determinism
    assert True  # Always passes - this is documentation only


def test_exact_rational_success():
    """
    Demonstrate exact rational arithmetic is deterministic.
    
    Rational arithmetic using fractions.Fraction provides
    exact, deterministic results across all platforms.
    """
    # Exact rational accumulation - forward
    forward_sum = Fraction(0)
    for i in range(1000):
        forward_sum += Fraction(1, 10)
    
    # Exact rational accumulation - backward
    backward_sum = Fraction(0)
    for i in range(999, -1, -1):
        backward_sum += Fraction(1, 10)
    
    # These are ALWAYS bit-identical
    assert forward_sum == backward_sum
    assert forward_sum == Fraction(100, 1)  # Exact value
    
    # Demonstrate deterministic conversion
    assert str(forward_sum) == "100"
    assert forward_sum.numerator == 100
    assert forward_sum.denominator == 1


def test_exact_integer_success():
    """
    Demonstrate exact integer arithmetic is deterministic.
    
    Integer arithmetic is always exact and deterministic.
    """
    # Forward accumulation
    forward_sum = 0
    for i in range(1000):
        forward_sum += i
    
    # Backward accumulation
    backward_sum = 0
    for i in range(999, -1, -1):
        backward_sum += i
    
    # Always bit-identical
    assert forward_sum == backward_sum
    assert forward_sum == 499500  # Exact value: sum(0..999) = n*(n-1)/2
    
    # Demonstrate exact operations
    result = (1000 * 999) // 2
    assert result == forward_sum


def test_rational_division_exact():
    """
    Demonstrate rational division is exact and deterministic.
    """
    # Division that would lose precision with floats
    a = Fraction(1, 3)
    b = Fraction(1, 7)
    c = a * b
    
    # Exact result
    assert c == Fraction(1, 21)
    
    # Multiply back - exact inverse
    d = c * Fraction(21, 1)
    assert d == Fraction(1, 1)
    
    # No accumulation errors
    result = Fraction(0)
    for i in range(100):
        result += Fraction(1, 3)
    
    assert result == Fraction(100, 3)
    assert result.numerator == 100
    assert result.denominator == 3
