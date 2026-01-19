"""
Invariant mining for the Spectrum deterministic framework.
"""

from __future__ import annotations
from typing import Iterable, Set, Tuple
from fractions import Fraction
from spectrum.invariants.core import Invariant


def mine(states: Iterable[Tuple[Fraction, ...]]) -> Set[Invariant]:
    states = tuple(states)
    if not states:
        return set()

    dim = len(states[0])
    invariants: set[Invariant] = set()

    # Constant invariants
    for i in range(dim):
        values = {s[i] for s in states}
        if len(values) == 1:
            invariants.add(
                Invariant((
                    "const",
                    (i,),
                    (values.pop(),),
                ))
            )

    # Equality invariants
    for i in range(dim):
        for j in range(i + 1, dim):
            if all(s[i] == s[j] for s in states):
                invariants.add(
                    Invariant((
                        "equal",
                        (i, j),
                        (),
                    ))
                )

    return invariants


__all__ = ["mine"]
