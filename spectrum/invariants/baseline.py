from spectrum.invariants.core import invariant


@invariant("non_empty_state")
def non_empty_state(state):
    return len(state) > 0


@invariant("no_time_dependency")
def no_time_dependency(state):
    return "time" not in state


@invariant("no_nondeterministic_sources")
def no_nondeterministic_sources(state: str) -> bool:
    """
    Invariant: state must not contain nondeterministic API calls.
    
    This checks for actual nondeterministic sources in executable code,
    not just vocabulary. Comments and documentation may freely use
    descriptive terms.
    """
    forbidden = [
        "numpy.random",
        "random.",
        "time.time(",
        "datetime.now(",
        "datetime.utcnow(",
        "uuid.",
        "secrets.",
        "os.environ",
    ]
    return not any(f in state for f in forbidden)
