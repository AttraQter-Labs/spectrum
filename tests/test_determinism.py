from spectrum.metrics.fairness import demographic_parity

def test_bit_identical():
    outputs = [1,0,1,1,0,0]
    groups = ["a","a","b","b","b","a"]

    r1 = demographic_parity(outputs, groups)
    r2 = demographic_parity(outputs, groups)

    assert r1 == r2
