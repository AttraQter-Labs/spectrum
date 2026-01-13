"""
Canonical serialization for deterministic lattice structures.

Guarantees:
- Order-independent input → identical bytes
- Stable across Python versions
- Hash-safe
"""

from typing import Iterable, Tuple
from fractions import Fraction
import hashlib
from spectrum.lattice.node import LatticeNode


def _serialize_fraction(f: Fraction) -> str:
    return f"{f.numerator}/{f.denominator}"


def serialize_node(node: LatticeNode) -> str:
    """
    Canonical string form of a node.
    """
    parents = ",".join(str(p) for p in sorted(node.parents))
    state = ",".join(_serialize_fraction(x) for x in node.state_vector)

    return f"id={node.id}|state={state}|parents={parents}"


def serialize_nodes(nodes: Iterable[LatticeNode]) -> Tuple[str, ...]:
    """
    Canonical ordered serialization of a node set.
    """
    return tuple(
        serialize_node(n)
        for n in sorted(nodes, key=lambda n: n.id)
    )


def hash_nodes(nodes: Iterable[LatticeNode]) -> str:
    """
    Stable SHA-256 hash of canonical serialization.
    """
    h = hashlib.sha256()
    for line in serialize_nodes(nodes):
        h.update(line.encode("utf-8"))
        h.update(b"\n")
    return h.hexdigest()
