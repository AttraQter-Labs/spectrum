"""Comprehensive determinism tests for Spectrum.

These tests verify that all functions produce bit-identical results
across multiple invocations, ensuring complete determinism.
"""

from fractions import Fraction
from spectrum.api import (
    demographic_parity_rates,
    demographic_parity_difference,
    demographic_parity_ratio,
    equal_opportunity_difference,
    create_trace,
    verify_trace,
)


def test_demographic_parity_rates_determinism():
    """Test that demographic_parity_rates produces identical results."""
    outputs = [1, 0, 1, 1, 0, 0]
    groups = ["a", "a", "b", "b", "b", "a"]
    
    # Run 10 times to ensure determinism
    results = [demographic_parity_rates(outputs, groups) for _ in range(10)]
    
    # All results should be identical
    first_result = results[0]
    for result in results[1:]:
        assert result == first_result, "Results must be bit-identical"
    
    # Verify exact Fraction outputs
    assert first_result["a"] == Fraction(1, 3)
    assert first_result["b"] == Fraction(2, 3)


def test_demographic_parity_difference_determinism():
    """Test that demographic_parity_difference produces identical results."""
    outputs = [1, 0, 1, 1, 0, 0, 1, 1]
    groups = ["A", "A", "B", "B", "B", "A", "A", "B"]
    
    # Run multiple times
    results = [demographic_parity_difference(outputs, groups) for _ in range(10)]
    
    # All results should be identical
    first_result = results[0]
    for result in results[1:]:
        assert result == first_result, "Results must be bit-identical"
    
    # Verify it's a Fraction
    assert isinstance(first_result, Fraction)
    assert first_result == Fraction(1, 4)


def test_demographic_parity_ratio_determinism():
    """Test that demographic_parity_ratio produces identical results."""
    outputs = [1, 1, 1, 0, 0, 0]
    groups = ["X", "Y", "Z", "X", "Y", "Z"]
    
    # Run multiple times
    results = [demographic_parity_ratio(outputs, groups) for _ in range(10)]
    
    # All results should be identical
    first_result = results[0]
    for result in results[1:]:
        assert result == first_result, "Results must be bit-identical"
    
    # Verify it's a Fraction
    assert isinstance(first_result, Fraction)


def test_equal_opportunity_difference_determinism():
    """Test that equal_opportunity_difference produces identical results."""
    outputs = [1, 0, 1, 1, 0, 1, 1, 0]
    labels = [1, 0, 1, 1, 0, 1, 1, 0]
    groups = ["M", "M", "F", "F", "M", "F", "M", "F"]
    
    # Run multiple times
    results = [
        equal_opportunity_difference(outputs, labels, groups) 
        for _ in range(10)
    ]
    
    # All results should be identical
    first_result = results[0]
    for result in results[1:]:
        assert result == first_result, "Results must be bit-identical"
    
    # Verify it's a Fraction
    assert isinstance(first_result, Fraction)


def test_trace_and_replay():
    """Test that traces capture deterministic execution and support replay verification."""
    outputs = [1, 0, 1]
    groups = ["A", "A", "B"]
    
    # Create first trace
    result1 = demographic_parity_rates(outputs, groups)
    inputs = {"outputs": outputs, "groups": groups}
    trace1 = create_trace("demographic_parity_rates", inputs, result1)
    
    # Create second trace from same computation
    result2 = demographic_parity_rates(outputs, groups)
    trace2 = create_trace("demographic_parity_rates", inputs, result2)
    
    # Results must be identical
    assert result1 == result2
    
    # Traces must be identical (bit-identical hashes)
    assert verify_trace(trace1, trace2), "Traces must be bit-identical"
    assert trace1["hash"] == trace2["hash"]
    
    # Run 10 more times to verify determinism
    for _ in range(10):
        result_n = demographic_parity_rates(outputs, groups)
        trace_n = create_trace("demographic_parity_rates", inputs, result_n)
        assert verify_trace(trace1, trace_n), "All traces must be bit-identical"


def test_fraction_exact_arithmetic():
    """Test that Fraction outputs provide exact arithmetic without floating-point errors."""
    outputs = [1, 1, 0]
    groups = ["A", "A", "A"]
    
    result = demographic_parity_rates(outputs, groups)
    rate = result["A"]
    
    # Verify it's exactly 2/3, not a float approximation
    assert rate == Fraction(2, 3)
    assert rate.numerator == 2
    assert rate.denominator == 3
    
    # Verify exact arithmetic: 3 * (2/3) == 2 exactly
    assert 3 * rate == Fraction(2, 1)
    
    # Test that 1/3 + 1/3 + 1/3 == 1 exactly (would fail with floats)
    third = Fraction(1, 3)
    assert third + third + third == Fraction(1, 1)


def test_no_nondeterminism_from_dict_ordering():
    """Test that dictionary ordering doesn't affect results (canonical ordering)."""
    # Try different orderings of groups
    outputs1 = [1, 0, 1, 0]
    groups1 = ["A", "B", "A", "B"]
    
    outputs2 = [0, 1, 0, 1]
    groups2 = ["B", "A", "B", "A"]
    
    result1 = demographic_parity_rates(outputs1, groups1)
    result2 = demographic_parity_rates(outputs2, groups2)
    
    # Both should produce same rates for each group
    assert result1["A"] == result2["A"]
    assert result1["B"] == result2["B"]
    
    # Results should have sorted keys (canonical ordering)
    assert list(result1.keys()) == sorted(result1.keys())
    assert list(result2.keys()) == sorted(result2.keys())


def test_empty_inputs():
    """Test deterministic behavior with edge cases."""
    # Empty inputs should not crash and should be deterministic
    outputs = []
    groups = []
    
    result1 = demographic_parity_rates(outputs, groups)
    result2 = demographic_parity_rates(outputs, groups)
    
    assert result1 == result2
    assert result1 == {}


def test_multiple_runs_identical():
    """Meta-test: Run all key functions multiple times and ensure identical results."""
    outputs = [1, 0, 1, 1, 0, 0, 1, 1, 0, 1]
    groups = ["A", "B", "A", "C", "B", "A", "C", "B", "C", "A"]
    labels = [1, 1, 1, 0, 0, 1, 1, 0, 1, 1]
    
    # Test each function 50 times
    for _ in range(50):
        r1 = demographic_parity_rates(outputs, groups)
        r2 = demographic_parity_rates(outputs, groups)
        assert r1 == r2
        
        d1 = demographic_parity_difference(outputs, groups)
        d2 = demographic_parity_difference(outputs, groups)
        assert d1 == d2
        
        ratio1 = demographic_parity_ratio(outputs, groups)
        ratio2 = demographic_parity_ratio(outputs, groups)
        assert ratio1 == ratio2
        
        eo1 = equal_opportunity_difference(outputs, labels, groups)
        eo2 = equal_opportunity_difference(outputs, labels, groups)
        assert eo1 == eo2
