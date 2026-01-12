from typing import Iterable
from spectrum.lattice.node import LatticeNode

def unique_node_ids(nodes: Iterable[LatticeNode]) -> bool:
    """
    Invariant: Node IDs must be globally unique.
    """
    ids = [n.node_id for n in nodes]
    return len(ids) == len(set(ids))
