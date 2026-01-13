"""
Execution that enforces canonical engine identity.
"""

from typing import Mapping, Any, Callable
from spectrum.engines import get_engine_spec
from spectrum.api.contracted_execute import execute_with_contract
from spectrum.contracts import Contract


def execute_engine(
    *,
    engine_name: str,
    engine_version: str,
    engine_fn: Callable,
    contract: Contract,
    state: Mapping[str, Any],
):
    spec = get_engine_spec(engine_name, engine_version, engine_fn)

    record = execute_with_contract(
        engine=f"{spec.name}@{spec.version}",
        state=state,
        contract=contract,
        fn=engine_fn,
    )

    return record
