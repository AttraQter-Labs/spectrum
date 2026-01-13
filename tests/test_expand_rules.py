from fractions import Fraction
from spectrum.lattice.node import LatticeNode
from spectrum.expand.rules import expand_deterministically
from spectrum.serialization.canonical import hash_nodes


def test_deterministic_expansion_structure():
    nodes = (
        LatticeNode(id=0, state_vector=(Fraction(0),), parents=set()),
        LatticeNode(id=1, state_vector=(Fraction(1),), parents=set()),
    )

    expanded = expand_deterministically(nodes, Fraction(1))

    assert len(expanded) == 2
    assert expanded[0].parents == {0}
    assert expanded[1].parents == {1}
    assert expanded[0].state_vector == (Fraction(1),)
    assert expanded[1].state_vector == (Fraction(2),)


def test_expansion_hash_stability():
    nodes = (
        LatticeNode(id=5, state_vector=(Fraction(3,2),), parents=set()),
        LatticeNode(id=2, state_vector=(Fraction(1),), parents=set()),
    )

    h1 = hash_nodes(expand_deterministically(nodes, Fraction(2)))
    h2 = hash_nodes(expand_deterministically(nodes, Fraction(2)))

    assert h1 == h2
