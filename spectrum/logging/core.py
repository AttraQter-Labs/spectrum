"""
Canonical deterministic execution log.

Rules:
- No timestamps
- No nondeterministic sources
- Content-addressed
"""

from dataclasses import dataclass, asdict
from typing import Mapping, Any, Dict
import hashlib
import json


def _canonical_json(obj: Any) -> str:
    return json.dumps(
        obj,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
    )


@dataclass(frozen=True)
class ExecutionRecord:
    engine: str
    input_state: Dict[str, Any]
    output: Any
    invariants: Dict[str, bool]
    digest: str


def _hash_record(payload: Dict[str, Any]) -> str:
    canonical = _canonical_json(payload)
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def record_execution(
    *,
    engine: str,
    input_state: Mapping[str, Any],
    output: Any,
    invariants: Mapping[str, bool],
) -> ExecutionRecord:
    if not isinstance(input_state, Mapping):
        raise TypeError("input_state must be a mapping")
    if not isinstance(invariants, Mapping):
        raise TypeError("invariants must be a mapping")

    payload = {
        "engine": engine,
        "input_state": dict(input_state),
        "output": output,
        "invariants": dict(invariants),
    }

    digest = _hash_record(payload)

    return ExecutionRecord(
        engine=engine,
        input_state=dict(input_state),
        output=output,
        invariants=dict(invariants),
        digest=digest,
    )
