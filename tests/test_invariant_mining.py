from fractions import Fraction

from spectrum.invariant.mine import mine


def test_constant_invariant():
    states = [
        ((Fraction(1), Fraction(2))),
        ((Fraction(1), Fraction(3))),
        ((Fraction(1), Fraction(4))),
    ]

    inv = mine(states)
    assert ("const", (0,), (Fraction(1),)) in inv


def test_equality_invariant():
    states = [
        ((Fraction(5), Fraction(5))),
        ((Fraction(7), Fraction(7))),
    ]

    inv = mine(states)
    assert ("equal", (0, 1), ()) in inv


def test_determinism():
    states = [
        ((Fraction(1, 2), Fraction(3, 4))),
        ((Fraction(1, 2), Fraction(5, 6))),
    ]

    r1 = mine(states)
    r2 = mine(states)
    assert r1 == r2
