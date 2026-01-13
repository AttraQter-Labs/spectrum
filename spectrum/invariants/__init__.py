"""
Invariant Registry

All invariants enforced by the Spectrum engine MUST be declared here.
"""

from spectrum.invariants.core import (
    INVARIANTS,
    check_invariants,
)

__all__ = [
    "INVARIANTS",
    "check_invariants",
]
