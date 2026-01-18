"""
Deterministic Invariant Miner
Phase 3.1 — Minimal Exact Implementation

Discovers invariants of the form:
- coordinate_i == constant
- coordinate_i == coordinate_j

All arithmetic is exact.
No randomness. No learning.
"""

from typing import Iterable, Tuple, Set
from fractions import Fraction
from spectrum.lattice.state import LatticeState


Invariant = Tuple[str, Tuple[int, ...], Tuple[Fraction, ...]]


def mine(states: Iterable[LatticeState]) -> Set[Invariant]:
    states = tuple(states)
    if not states:
        return set()

    dim = states[0].dimension()
    coords = [s.coordinates for s in states]

    invariants: Set[Invariant] = set()

    # Constant-coordinate invariants
    for i in range(dim):
        values = {c[i] for c in coords}
        if len(values) == 1:
            invariants.add((
                "const",
                (i,),
                (next(iter(values)),)
            ))

    # Equality invariants
    for i in range(dim):
        for j in range(i + 1, dim):
            if all(c[i] == c[j] for c in coords):
                invariants.add((
                    "equal",
                    (i, j),
                    ()
                ))

    return invariants
