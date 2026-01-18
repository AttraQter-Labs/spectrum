"""
Deterministic Irreversibility Detector — basic skeleton.
"""

from typing import Iterable, Tuple
from dataclasses import dataclass
from fractions import Fraction
from . import entropy_shift, is_irreversible

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
        before = [float(x) for x in t.parent_state]
        after = [float(x) for x in t.child_state]
        if is_irreversible(np.array(before), np.array(after), threshold):
            result.append(t)
    return tuple(result)
    
