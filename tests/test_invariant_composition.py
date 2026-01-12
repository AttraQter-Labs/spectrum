from fractions import Fraction
from spectrum.lattice.node import LatticeNode
from spectrum.invariants.compose import all_invariants_hold
from spectrum.invariants.core import unique_node_ids
from spectrum.boundary.checks import no_orphan_nodes

def test_composed_invariants_pass():
    nodes = [
        LatticeNode(0, (Fraction(0),), set(), None, b""),
        LatticeNode(1, (Fraction(1),), {0}, None, b""),
    ]
    assert all_invariants_hold(
        nodes,
        [unique_node_ids, no_orphan_nodes],
    )

def test_composed_invariants_fail():
    nodes = [
        LatticeNode(0, (Fraction(0),), set(), None, b""),
        LatticeNode(0, (Fraction(1),), set(), None, b""),
    ]
    assert not all_invariants_hold(
        nodes,
        [unique_node_ids, no_orphan_nodes],
    )
