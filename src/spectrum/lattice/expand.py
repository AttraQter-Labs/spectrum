"""
Deterministic lattice expansion.
"""

from typing import Iterable


def expand(state) -> Iterable:
    """
    Deterministically expand a lattice state.
    """
    # Identity expansion for deterministic baseline
    yield state
