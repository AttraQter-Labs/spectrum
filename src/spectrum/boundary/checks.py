from typing import Iterable
from spectrum.lattice.node import LatticeNode

def no_orphan_nodes(nodes: Iterable[LatticeNode]) -> bool:
    """
    Boundary invariant:
    Every node except root must have at least one parent.
    """
    nodes = tuple(nodes)
    if not nodes:
        return True

    root_ids = {n.node_id for n in nodes if not n.parent_ids}
    return len(root_ids) == 1
