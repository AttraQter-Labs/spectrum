from fractions import Fraction
from spectrum.lattice.node import LatticeNode
from spectrum.serialization.canonical import (
    serialize_node,
    serialize_nodes,
    hash_nodes,
)


def test_node_serialization_stable():
    n1 = LatticeNode(id=1, state_vector=(Fraction(1,2),), parents={0})
    n2 = LatticeNode(id=1, state_vector=(Fraction(1,2),), parents={0})
    assert serialize_node(n1) == serialize_node(n2)


def test_set_order_independent():
    a = LatticeNode(id=1, state_vector=(Fraction(0),), parents=set())
    b = LatticeNode(id=2, state_vector=(Fraction(1),), parents={1})

    s1 = serialize_nodes([a, b])
    s2 = serialize_nodes([b, a])

    assert s1 == s2


def test_hash_deterministic():
    nodes = [
        LatticeNode(id=3, state_vector=(Fraction(2),), parents={1}),
        LatticeNode(id=1, state_vector=(Fraction(0),), parents=set()),
    ]

    h1 = hash_nodes(nodes)
    h2 = hash_nodes(list(reversed(nodes)))

    assert h1 == h2
    assert len(h1) == 64
