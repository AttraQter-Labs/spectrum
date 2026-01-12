from fractions import Fraction
from spectrum.boundary.map import map_boundaries

def test_boundary_mapper_is_deterministic():
    params = (
        (Fraction(0), Fraction(1)),
        (Fraction(1, 2), Fraction(3, 4)),
    )

    r1 = map_boundaries(params)
    r2 = map_boundaries(params)

    assert r1 == r2
