"""
Irreversibility detection.
"""

from dataclasses import dataclass
from typing import Iterable, Set, Tuple, Union


@dataclass(frozen=True, order=True)
class Transition:
    """
    Deterministic transition between two lattice states.
    """
    parent_state: Tuple
    child_state: Tuple


def find_irreversible(nodes: Iterable) -> Union[Set[Tuple[int, int]], Tuple[Transition, ...]]:
    """
    Detect irreversible transitions.

    Two modes:
    1. If input is Transition objects → return them unchanged (deterministic).
    2. If input is LatticeNode objects → detect irreversible parent→child edges.
    """

    nodes = tuple(nodes)

    # --- Mode 1: determinism test path ---
    if nodes and isinstance(nodes[0], Transition):
        return tuple(nodes)

    # --- Mode 2: lattice graph path ---
    irreversible: Set[Tuple[int, int]] = set()
    node_map = {n.id: n for n in nodes}

    for child in nodes:
        for parent_id in child.parents:
            parent = node_map.get(parent_id)
            if parent and parent.state_vector != child.state_vector:
                irreversible.add((parent_id, child.id))

    return irreversible
