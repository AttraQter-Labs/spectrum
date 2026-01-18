"""
Global lattice invariants.

All invariants must be:
- Deterministic
- Order-independent
- Environment-independent
"""

from typing import Iterable
from spectrum.lattice.node import LatticeNode


def unique_node_ids(nodes: Iterable[LatticeNode]) -> bool:
    ids = [n.id for n in nodes]
    return len(ids) == len(set(ids))


def no_orphan_nodes(nodes: Iterable[LatticeNode]) -> bool:
    node_ids = {n.id for n in nodes}
    for n in nodes:
        for p in n.parents:
            if p not in node_ids:
                return False
    return True


def parents_are_acyclic(nodes: Iterable[LatticeNode]) -> bool:
    graph = {n.id: set(n.parents) for n in nodes}

    visited = set()
    stack = set()

    def visit(nid):
        if nid in stack:
            return False
        if nid in visited:
            return True
        stack.add(nid)
        for p in graph.get(nid, []):
            if not visit(p):
                return False
        stack.remove(nid)
        visited.add(nid)
        return True

    return all(visit(n.id) for n in nodes)
