"""
Spectrum Public API

This module defines the ONLY supported public interface.

Stability contract:
- Versioned at v3.0-interface-boundary
- Deterministic
- Non-learning
- Replayable
"""

from spectrum.api.measure import measure
from spectrum.api.verify import verify

__all__ = [
    "measure",
    "verify",
]
