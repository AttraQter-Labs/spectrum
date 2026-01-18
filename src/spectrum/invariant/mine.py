"""
Invariant mining.
"""

from typing import Iterable, Tuple


def mine(states: Iterable) -> Tuple:
    """
    Deterministically mine invariants from states.
    """
    states = tuple(states)

    invariants = set()

    # Constant invariants
    for idx in range(len(states[0])):
        values = {s[idx] for s in states}
        if len(values) == 1:
            invariants.add(("const", (idx,), tuple(values)))

    # Equality invariants
    for i in range(len(states[0])):
        for j in range(i + 1, len(states[0])):
            if all(s[i] == s[j] for s in states):
                invariants.add(("equal", (i, j), ()))

    return tuple(sorted(invariants))
