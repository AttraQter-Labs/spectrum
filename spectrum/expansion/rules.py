"""
Deterministic lattice expansion rules.

Rules:
- Pure function
- No nondeterministic sources
- No time
- Canonical ordering
- Expansion depends ONLY on input state
"""

from fractions import Fraction
from typing import Iterable, Tuple
from spectrum.lattice.node import LatticeNode


def expand_node(node: LatticeNode) -> Tuple[LatticeNode, ...]:
    """
    Canonical deterministic expansion:
    - Each node expands into exactly one child
    - Child state = state_vector + (1,)
    - Parent relationship preserved deterministically
    """

    next_id = node.id * 2 + 1  # canonical, collision-free
    next_state = node.state_vector + (Fraction(1),)

    child = LatticeNode(
        id=next_id,
        state_vector=next_state,
        parents={node.id},
    )

    return (child,)


def expand_layer(nodes: Iterable[LatticeNode]) -> Tuple[LatticeNode, ...]:
    """
    Deterministic layer expansion.
    Output is sorted by node id for canonical ordering.
    """

    expanded = []
    for n in nodes:
        expanded.extend(expand_node(n))

    return tuple(sorted(expanded, key=lambda n: n.id))
