import numpy as np
from spectrum.irreversibility import entropy_shift, is_irreversible

def test_entropy_shift_sign():
    a = np.array([0.7, 0.3])
    b = np.array([0.5, 0.5])
    assert entropy_shift(a, b) > 0    # entropy should increase

def test_irreversible_flag():
    a = np.array([0.9, 0.1])
    b = np.array([0.5, 0.5])
    assert is_irreversible(a, b)
