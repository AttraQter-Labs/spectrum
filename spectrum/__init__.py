"""Spectrum - Deterministic Measurement Infrastructure

A deterministic lattice explorer providing exact, reproducible fairness metrics
using rational arithmetic. No randomness, no floating point imprecision, 
no time dependence - just bit-identical results every time.
"""

__version__ = "0.1.0"

from spectrum.api import *

__all__ = ["__version__"]
