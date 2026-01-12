from fractions import Fraction
from spectrum.lattice.node import LatticeNode
from spectrum.boundary.checks import no_orphan_nodes
from spectrum.invariants.core import unique_node_ids

def test_unique_node_ids():
    nodes = [
        LatticeNode(0, (Fraction(0),), set(), None, b""),
        LatticeNode(1, (Fraction(1),), {0}, None, b""),
    ]
    assert unique_node_ids(nodes)

def test_no_orphan_nodes_valid():
    nodes = [
        LatticeNode(0, (Fraction(0),), set(), None, b""),
        LatticeNode(1, (Fraction(1),), {0}, None, b""),
    ]
    assert no_orphan_nodes(nodes)

def test_no_orphan_nodes_invalid():
    nodes = [
        LatticeNode(0, (Fraction(0),), set(), None, b""),
        LatticeNode(1, (Fraction(1),), set(), None, b""),
    ]
    assert not no_orphan_nodes(nodes)
