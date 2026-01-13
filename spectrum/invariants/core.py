"""
Core invariant definitions.

Rules:
- Deterministic
- Pure
- Side-effect free
"""

from typing import Callable, Dict, Mapping


Invariant = Callable[[Mapping[str, object]], bool]

INVARIANTS: Dict[str, Invariant] = {}


def invariant(name: str) -> Callable[[Invariant], Invariant]:
    """
    Decorator to register an invariant.
    """
    def register(fn: Invariant) -> Invariant:
        if name in INVARIANTS:
            raise ValueError(f"Invariant already registered: {name}")
        INVARIANTS[name] = fn
        return fn
    return register


def check_invariants(state: Mapping[str, object]) -> Dict[str, bool]:
    """
    Evaluate all registered invariants.

    Returns a dict:
        invariant_name -> pass/fail
    """
    if not isinstance(state, Mapping):
        raise TypeError("state must be a mapping")

    results: Dict[str, bool] = {}
    for name, inv in INVARIANTS.items():
        results[name] = bool(inv(state))
    return results
