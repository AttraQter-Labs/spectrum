"""
Deterministic invariant verification.
"""

from typing import Mapping
from spectrum.invariants import check_invariants


def verify(state: Mapping[str, object]) -> bool:
    """
    Verify all registered invariants.

    Deterministic. Total.
    """
    results = check_invariants(state)
    return all(results.values())
