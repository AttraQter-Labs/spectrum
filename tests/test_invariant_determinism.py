from fractions import Fraction
from spectrum.invariants.mine import mine

def test_invariant_miner_is_deterministic():
    states = (
        (Fraction(1, 2), Fraction(3, 4)),
        (Fraction(1, 2), Fraction(3, 4)),
    )
    r1 = mine(states)
    r2 = mine(states)
    assert r1 == r2
