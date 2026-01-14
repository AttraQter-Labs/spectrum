"""
Deterministic verification module.

Verifies bit-for-bit equality of replay outputs.
"""

from spectrum.replay import run


def verify(input_bytes: bytes, claimed_output: bytes) -> bool:
    """
    Verify claimed output against deterministic recomputation.
    
    Recomputes run(input_bytes) and compares bit-for-bit equality.
    
    Args:
        input_bytes: Original input
        claimed_output: Output to verify
        
    Returns:
        True if and only if claimed_output is bit-identical to run(input_bytes)
        
    Guarantees:
        - Deterministic verification
        - Bit-for-bit comparison
        - No tolerance or approximation
    """
    actual_output = run(input_bytes)
    return actual_output == claimed_output
