"""
Irreversibility‑classification layer for the Spectrum deterministic framework.
Provides helpers to test entropy growth, replay stability, and irreversible transitions.
"""
from __future__ import annotations
import numpy as np

def entropy_shift(before: np.ndarray, after: np.ndarray) -> float:
    """Return entropy difference between two states."""
    before_p = before / before.sum()
    after_p = after / after.sum()
    h_before = -(before_p * np.log2(before_p + 1e-12)).sum()
    h_after  = -(after_p  * np.log2(after_p + 1e-12)).sum()
    return h_after - h_before

def is_irreversible(before: np.ndarray, after: np.ndarray, threshold: float = 0.01) -> bool:
    """True if entropy increases by more than the given threshold."""
    return entropy_shift(before, after) > threshold
    
