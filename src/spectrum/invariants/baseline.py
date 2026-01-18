from spectrum.invariants.core import invariant


@invariant("non_empty_state")
def non_empty_state(state):
    return len(state) > 0


@invariant("no_time_dependency")
def no_time_dependency(state):
    return "time" not in state


@invariant("no_randomness")
def no_randomness(state):
    return "random" not in state
