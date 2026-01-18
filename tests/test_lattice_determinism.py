from fractions import Fraction

from spectrum.lattice.expand import expand

def test_expand_is_deterministic():
    s = ((Fraction(1, 2), Fraction(3, 4)))
    r1 = tuple(expand(s))
    r2 = tuple(expand(s))
    assert r1 == r2
