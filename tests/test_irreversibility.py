import numpy as np
from spectrum.irreversibility import entropy_shift, is_irreversible
from spectrum.irreversibility.detect import Transition, find_irreversible
from fractions import Fraction

def test_entropy_shift_sign():
    a = np.array([0.7, 0.3])
    b = np.array([0.5, 0.5])
    assert entropy_shift(a, b) > 0

def test_irreversible_flag():
    a = np.array([0.9, 0.1])
    b = np.array([0.5, 0.5])
    assert is_irreversible(a, b)

def test_find_irreversible_detects_growth():
    transitions = [
        Transition((Fraction(9,10), Fraction(1,10)), (Fraction(1,2), Fraction(1,2))),
        Transition((Fraction(1,2), Fraction(1,2)), (Fraction(9,10), Fraction(1,10))),
    ]
    res = find_irreversible(transitions)
    assert len(res) == 1
    assert res[0].child_state == (Fraction(1,2), Fraction(1,2))
