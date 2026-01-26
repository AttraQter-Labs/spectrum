"""
Deterministic Irreversibility Detector — basic skeleton.
"""

import numpy as np
from typing import Iterable, Tuple
from dataclasses import dataclass
from fractions import Fraction
from .entropy_shift import entropy_shift  # Adjusted import
from .is_irreversible import is_irreversible  # Adjusted import

@dataclass(frozen=True)
class Transition:
    """Immutable transition placeholder."""
    parent_state: Tuple[Fraction, ...]
    child_state: Tuple[Fraction, ...]

def find_irreversible(
    transitions: Iterable[Transition],
    threshold: float = 0.01,
):
    """Return the subset of transitions showing entropy increase > threshold."""
    result = []
    for t in transitions:
        # Convert states to NumPy arrays to calculate entropy differences
        before = np.array([float(x) for x in t.parent_state])
        after = np.array([float(x) for x in t.child_state])
        # Check irreversibility and append to result if above the threshold
        if is_irreversible(before, after, threshold):
            result.append(t)
    return tuple(result)
