"""
Invariant core utilities for the Spectrum deterministic framework.

This module provides helper functions and lightweight structures
for identifying, composing, and validating invariants within
state lattices and transition graphs.

It is written to be side‑effect‑free and reproducible, forming the
base for higher‑level mining and verification modules.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Iterable, Iterator, Mapping, Sequence, Set


# ---------------------------------------------------------------------
# Basic helpers
# ---------------------------------------------------------------------

def unique_node_ids(nodes: Iterable[Any]) -> Set[Any]:
    """
    Return a set of unique node identifiers from any iterable.

    Example:
        >>> unique_node_ids([1, 2, 2, 3])
        {1, 2, 3}
    """
    return set(nodes)


def compose_invariants(*invariants: Mapping[Any, Any]) -> dict[Any, Any]:
    """
    Combine multiple invariant mappings into one, preferring later values
    when keys overlap (right‑biased union).

    Example:
        >>> compose_invariants({'a': 1}, {'b': 2}, {'a': 3})
        {'a': 3, 'b': 2}
    """
    result: dict[Any, Any] = {}
    for inv in invariants:
        result.update(inv)
    return result


def flatten_invariants(nested: Iterable[Iterable[Any]]) -> list[Any]:
    """
    Flatten nested invariant collections into a single list.

    Example:
        >>> flatten_invariants([[1, 2], [3]])
        [1, 2, 3]
    """
    return [item for group in nested for item in group]


# ---------------------------------------------------------------------
# Structured invariant representation
# ---------------------------------------------------------------------

@dataclass(frozen=True)
class Invariant:
    """
    Represents a single invariant as an (id, value) pair.
    Useful for conversion or equality‑based tests.
    """
    identifier: Any
    value: Any

    def __iter__(self) -> Iterator[Any]:
        yield self.identifier
        yield self.value

    def as_tuple(self) -> tuple[Any, Any]:
        return (self.identifier, self.value)


def to_invariants(mapping: Mapping[Any, Any]) -> tuple[Invariant, ...]:
    """
    Convert a mapping into a tuple of Invariant objects.
    """
    return tuple(Invariant(k, v) for k, v in mapping.items())


def invariant_difference(
    a: Mapping[Any, Any], b: Mapping[Any, Any]
) -> dict[Any, Any]:
    """
    Determine elements unique to the first invariant mapping.

    Example:
        >>> invariant_difference({'x': 1, 'y': 2}, {'y': 2})
        {'x': 1}
    """
    diff = {}
    for key, val in a.items():
        if key not in b or b[key] != val:
            diff[key] = val
    return diff


# ---------------------------------------------------------------------
# Consistency checks
# ---------------------------------------------------------------------

def verify_composition_consistency(*invariants: Mapping[Any, Any]) -> bool:
    """
    True if all invariants can be composed without conflicting values
    for the same keys.
    """
    seen: dict[Any, Any] = {}
    for inv in invariants:
        for k, v in inv.items():
            if k in seen and seen[k] != v:
                return False
            seen[k] = v
    return True


# ---------------------------------------------------------------------
# Export list
# ---------------------------------------------------------------------

__all__ = [
    "unique_node_ids",
    "compose_invariants",
    "flatten_invariants",
    "Invariant",
    "to_invariants",
    "invariant_difference",
    "verify_composition_consistency",
]
