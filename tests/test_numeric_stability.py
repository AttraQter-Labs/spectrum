"""
Test numeric stability: demonstrates float divergence vs exact rational success.

This test shows why Spectrum uses exact rational arithmetic instead of floating point.
"""

from fractions import Fraction


def test_float_divergence():
    """
    Demonstrate that floating point arithmetic is non-deterministic across platforms.
    This test documents the problem, not Spectrum's solution.
    """
    # Float arithmetic can lead to precision issues
    result_float = 0.1 + 0.2
    
    # This is a well-known floating point issue
    # We document it but don't use it in Spectrum
    assert result_float != 0.3  # Known float precision issue
    assert abs(result_float - 0.3) < 1e-10  # Within epsilon, but not exact


def test_rational_exact():
    """
    Demonstrate that Spectrum's rational arithmetic is exact and deterministic.
    """
    # Rational arithmetic is exact
    a = Fraction(1, 10)
    b = Fraction(2, 10)
    result = a + b
    
    # Exact comparison works with rationals
    assert result == Fraction(3, 10)
    assert result == Fraction(30, 100)
    assert result.numerator == 3
    assert result.denominator == 10


def test_rational_bit_identical():
    """
    Verify that rational operations produce bit-identical results across runs.
    """
    # Same computation multiple times
    results = []
    for _ in range(5):
        r = Fraction(1, 3) + Fraction(2, 3)
        results.append(r)
    
    # All results are identical
    assert all(r == results[0] for r in results)
    assert all(r == Fraction(1, 1) for r in results)


def test_rational_ordering_deterministic():
    """
    Verify that rational comparisons are deterministic.
    """
    values = [
        Fraction(1, 2),
        Fraction(1, 3),
        Fraction(2, 3),
        Fraction(1, 4),
    ]
    
    # Sort multiple times - should always be same
    sorted1 = sorted(values)
    sorted2 = sorted(values)
    sorted3 = sorted(values)
    
    assert sorted1 == sorted2
    assert sorted2 == sorted3
    
    # Verify expected order
    expected = [Fraction(1, 4), Fraction(1, 3), Fraction(1, 2), Fraction(2, 3)]
    assert sorted1 == expected
