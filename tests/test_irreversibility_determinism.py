from fractions import Fraction
from spectrum.irreversibility.detect import Transition, find_irreversible

def test_irreversibility_detector_is_deterministic():
    t = Transition(
        parent_state=(Fraction(1, 2),),
        child_state=(Fraction(3, 4),),
    )
    transitions = (t,)

    r1 = find_irreversible(transitions)
    r2 = find_irreversible(transitions)

    assert r1 == r2
