"""
Deterministic expansion rules for lattice growth.
"""

from typing import Iterable, Tuple
from fractions import Fraction
from spectrum.lattice.node import LatticeNode


def apply_rule_add_constant(
    node: LatticeNode,
    constant: Fraction,
    next_id: int,
) -> LatticeNode:
    """
    Deterministically add a constant to all state components.
    """
    new_state = tuple(x + constant for x in node.state_vector)

    return LatticeNode(
        id=next_id,
        state_vector=new_state,
        parents={node.id},
        transition_rule=f"add({constant})",
        causal_input_hash=b"",
    )


def expand_deterministically(
    nodes: Iterable[LatticeNode],
    constant: Fraction,
) -> Tuple[LatticeNode, ...]:
    """
    Expand lattice by applying a single deterministic rule
    to all nodes in canonical order.
    """
    sorted_nodes = sorted(nodes, key=lambda n: n.id)
    max_id = max(n.id for n in sorted_nodes)

    children = []
    for offset, node in enumerate(sorted_nodes, start=1):
        child = apply_rule_add_constant(
            node=node,
            constant=constant,
            next_id=max_id + offset,
        )
        children.append(child)

    return tuple(children)
