from dataclasses import dataclass
from typing import Tuple, Set, Optional
from fractions import Fraction

@dataclass(frozen=True)
class LatticeNode:
    """
    Deterministic lattice node (Phase 3 canonical).
    """
    node_id: int
    state_vector: Tuple[Fraction, ...]
    parent_ids: Set[int]
    transition_rule: Optional[object]
    causal_input_hash: bytes
