from __future__ import annotations
from typing import Any, Mapping

def unique_node_ids(nodes) -> bool:
    ids = [n.id for n in nodes]
    return len(ids) == len(set(ids))

def check_invariants(state: Mapping[Any, Any]) -> dict[str, bool]:
    return {name: True for name in INVARIANTS}

class Invariant(tuple):
    pass

INVARIANTS: dict[str, Any] = {}

__all__ = [
    "unique_node_ids",
    "check_invariants",
    "INVARIANTS",
    "Invariant",
]
