"""
Execution with enforced interface contracts.
"""

from typing import Mapping, Any, Callable
from spectrum.contracts import Contract, enforce_contract
from spectrum.logging import record_execution
from spectrum.invariants import check_invariants


def execute_with_contract(
    *,
    engine: str,
    state: Mapping[str, Any],
    contract: Contract,
    fn: Callable,
):
    invariant_results = check_invariants(state)
    if not all(invariant_results.values()):
        raise AssertionError("Invariant violation")

    safe_fn = enforce_contract(contract, fn)
    output = safe_fn(state)

    return record_execution(
        engine=engine,
        input_state=state,
        output=output,
        invariants=invariant_results,
    )
