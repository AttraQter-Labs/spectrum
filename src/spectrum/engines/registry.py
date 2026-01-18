"""
Engine registry with version sealing.

Rules:
- Engines must be declared here to be executable
- Version is immutable once released
- Engine identity is (name, version, code_hash)
"""

from dataclasses import dataclass
from typing import Dict
import hashlib
import inspect


@dataclass(frozen=True)
class EngineSpec:
    name: str
    version: str
    code_hash: str
    description: str


def _hash_callable(fn) -> str:
    src = inspect.getsource(fn).encode("utf-8")
    return hashlib.sha256(src).hexdigest()


# --- Canonical engine registry ---
ENGINE_REGISTRY: Dict[str, EngineSpec] = {}


def register_engine(*, name: str, version: str, fn, description: str) -> None:
    engine_id = f"{name}@{version}"
    code_hash = _hash_callable(fn)

    if engine_id in ENGINE_REGISTRY:
        raise AssertionError(f"Engine already registered: {engine_id}")

    ENGINE_REGISTRY[engine_id] = EngineSpec(
        name=name,
        version=version,
        code_hash=code_hash,
        description=description,
    )


def get_engine_spec(name: str, version: str, fn) -> EngineSpec:
    engine_id = f"{name}@{version}"

    if engine_id not in ENGINE_REGISTRY:
        raise KeyError(f"Unknown engine: {engine_id}")

    spec = ENGINE_REGISTRY[engine_id]
    current_hash = _hash_callable(fn)

    if spec.code_hash != current_hash:
        raise AssertionError(
            f"Engine code hash mismatch for {engine_id}"
        )

    return spec
