"""
Deterministic replay module.

Pure function for bit-identical reproducibility.
No external calls, no randomness, no time, no environment/state.
"""

import hashlib


def run(input_bytes: bytes) -> bytes:
    """
    Pure deterministic function that transforms input to output.
    
    Output is derived only from input_bytes using deterministic,
    pure logic (cryptographic hash).
    
    Args:
        input_bytes: Raw input bytes
        
    Returns:
        Deterministic output bytes derived from input
        
    Guarantees:
        - Bit-identical output for identical input
        - No randomness
        - No time dependence
        - No environment dependence
        - No external state
    """
    # Use SHA-256 for deterministic, cryptographic transformation
    # This ensures bit-identical results across all platforms and runs
    return hashlib.sha256(input_bytes).digest()
