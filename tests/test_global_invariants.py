from fractions import Fraction
from spectrum.lattice.node import LatticeNode
from spectrum.invariants.global_invariants import (
    unique_node_ids,
    no_orphan_nodes,
    parents_are_acyclic,
)


def test_global_invariants_pass():
    nodes = [
        LatticeNode(id=0, state_vector=(Fraction(0),), parents=set()),
        LatticeNode(id=1, state_vector=(Fraction(1),), parents={0}),
        LatticeNode(id=2, state_vector=(Fraction(2),), parents={1}),
    ]

    assert unique_node_ids(nodes)
    assert no_orphan_nodes(nodes)
    assert parents_are_acyclic(nodes)


def test_cycle_detected():
    nodes = [
        LatticeNode(id=0, state_vector=(Fraction(0),), parents={1}),
        LatticeNode(id=1, state_vector=(Fraction(1),), parents={0}),
    ]

    assert not parents_are_acyclic(nodes)
