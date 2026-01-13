from spectrum.api.execute import execute


def identity(state):
    return state


def test_execution_is_deterministic():
    state = {"x": 1}

    r1 = execute("test-engine", state, identity)
    r2 = execute("test-engine", state, identity)

    assert r1.digest == r2.digest
    assert r1.input_state == r2.input_state
    assert r1.output == r2.output
