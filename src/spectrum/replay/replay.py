"""
Deterministic replay engine for canonical lattice states.
"""

from typing import Iterable, Tuple
from fractions import Fraction
from spectrum.lattice.node import LatticeNode


def parse_fraction(s: str) -> Fraction:
    num, den = s.split("/")
    return Fraction(int(num), int(den))


def parse_node(line: str) -> LatticeNode:
    """
    Parse canonical node serialization.
    """
    parts = dict(p.split("=", 1) for p in line.split("|"))

    node_id = int(parts["id"])

    state = tuple(
        parse_fraction(x)
        for x in parts["state"].split(",")
        if x
    )

    parents = (
        set(int(x) for x in parts["parents"].split(","))
        if parts["parents"]
        else set()
    )

    return LatticeNode(
        id=node_id,
        state_vector=state,
        parents=parents,
        transition_rule=None,
        causal_input_hash=b"",
    )


def replay_nodes(serialized: Iterable[str]) -> Tuple[LatticeNode, ...]:
    """
    Deterministically reconstruct nodes from canonical serialization.
    """
    nodes = tuple(parse_node(line) for line in serialized)
    return tuple(sorted(nodes, key=lambda n: n.id))
