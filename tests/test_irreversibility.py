from fractions import Fraction
from spectrum.lattice.node import LatticeNode
from spectrum.irreversibility.detect import find_irreversible


def test_irreversible_transition_detected():
    n0 = LatticeNode(
        node_id=0,
        state_vector=(Fraction(0),),
        parent_ids=set(),
        transition_rule=None,
        causal_input_hash=b""
    )

    n1 = LatticeNode(
        node_id=1,
        state_vector=(Fraction(1),),
        parent_ids={0},
        transition_rule=None,
        causal_input_hash=b""
    )

    irreversible = find_irreversible([n0, n1])
    assert (0, 1) in irreversible


def test_reversible_not_flagged():
    n0 = LatticeNode(0, (Fraction(0),), set(), None, b"")
    n1 = LatticeNode(1, (Fraction(0),), {0}, None, b"")
    n2 = LatticeNode(2, (Fraction(0),), {0}, None, b"")

    irreversible = find_irreversible([n0, n1, n2])
    assert irreversible == set()


def test_determinism():
    n0 = LatticeNode(0, (Fraction(0),), set(), None, b"")
    n1 = LatticeNode(1, (Fraction(1),), {0}, None, b"")

    r1 = find_irreversible([n0, n1])
    r2 = find_irreversible([n0, n1])

    assert r1 == r2
