"""
Deterministic execution wrapper with audit logging.
"""

from typing import Mapping, Any
from spectrum.api.verify import verify
from spectrum.invariants import check_invariants
from spectrum.logging import record_execution


def execute(engine: str, state: Mapping[str, Any], fn) -> Any:
    """
    Execute a deterministic function under invariant enforcement.
    """
    invariant_results = check_invariants(state)
    if not all(invariant_results.values()):
        raise AssertionError("Invariant violation")

    output = fn(state)

    record = record_execution(
        engine=engine,
        input_state=state,
        output=output,
        invariants=invariant_results,
    )

    return record
