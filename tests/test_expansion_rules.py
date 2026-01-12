from fractions import Fraction
from spectrum.lattice.node import LatticeNode
from spectrum.expansion.rules import expand_node, expand_layer


def test_single_node_expansion_deterministic():
    n = LatticeNode(id=1, state_vector=(Fraction(0),), parents=set())
    c1 = expand_node(n)
    c2 = expand_node(n)
    assert c1 == c2


def test_expansion_properties():
    n = LatticeNode(id=2, state_vector=(Fraction(3),), parents=set())
    child = expand_node(n)[0]

    assert child.parents == {2}
    assert child.state_vector[-1] == Fraction(1)
    assert child.id == 5


def test_layer_expansion_order_independent():
    n1 = LatticeNode(id=1, state_vector=(Fraction(0),), parents=set())
    n2 = LatticeNode(id=3, state_vector=(Fraction(1),), parents=set())

    out1 = expand_layer([n1, n2])
    out2 = expand_layer([n2, n1])

    assert out1 == out2
    assert tuple(n.id for n in out1) == tuple(sorted(n.id for n in out1))
