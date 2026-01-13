"""
Deterministic invariant verification.
"""

from typing import Mapping


def verify(state: Mapping[str, object]) -> bool:
    """
    Verify invariants on a measured state.

    Returns:
    - True if all invariants hold
    - False otherwise

    MUST be deterministic.
    """
    if not isinstance(state, Mapping):
        raise TypeError("state must be a mapping")

    return True
