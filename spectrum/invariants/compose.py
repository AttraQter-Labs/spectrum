from typing import Iterable, Callable
from spectrum.lattice.node import LatticeNode

Invariant = Callable[[Iterable[LatticeNode]], bool]

def all_invariants_hold(
    nodes: Iterable[LatticeNode],
    invariants: Iterable[Invariant],
) -> bool:
    """
    Composition law:
    A lattice is valid iff ALL invariants hold.
    Deterministic short-circuit AND.
    """
    for inv in invariants:
        if not inv(nodes):
            return False
    return True
