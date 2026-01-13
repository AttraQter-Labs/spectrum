"""
Deterministic interface contracts.

Rules:
- Explicit input schema
- Explicit output schema
- Explicit forbidden behavior
- No implicit coercion
"""

from dataclasses import dataclass
from typing import Callable, Mapping, Any, Tuple


@dataclass(frozen=True)
class Contract:
    name: str
    input_keys: Tuple[str, ...]
    output_type: type
    forbidden_keys: Tuple[str, ...] = ()

    def validate_input(self, data: Mapping[str, Any]) -> None:
        if not isinstance(data, Mapping):
            raise TypeError("Input must be a mapping")

        for key in self.input_keys:
            if key not in data:
                raise KeyError(f"Missing required key: {key}")

        for key in self.forbidden_keys:
            if key in data:
                raise AssertionError(f"Forbidden key present: {key}")

    def validate_output(self, output: Any) -> None:
        if not isinstance(output, self.output_type):
            raise TypeError(
                f"Output must be {self.output_type.__name__}, "
                f"got {type(output).__name__}"
            )


def enforce_contract(contract: Contract, fn: Callable) -> Callable:
    def wrapped(state):
        contract.validate_input(state)
        result = fn(state)
        contract.validate_output(result)
        return result
    return wrapped
