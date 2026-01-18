from dataclasses import dataclass
from typing import Tuple, Set, Optional

@dataclass(frozen=True)
class LatticeNode:
    """
    Deterministic lattice node.

    Canonical fields:
      - id
      - state_vector
      - parents
      - transition_rule
      - causal_input_hash

    Backward-compatible with legacy test constructors:
      - node_id
      - parent_ids
    """

    id: int
    state_vector: Tuple
    parents: Set[int]
    transition_rule: Optional[object] = None
    causal_input_hash: bytes = b""

    def __init__(
        self,
        id: int = None,
        state_vector: Tuple = None,
        parents: Set[int] = None,
        transition_rule: Optional[object] = None,
        causal_input_hash: bytes = b"",
        *,
        node_id: int = None,
        parent_ids: Set[int] = None,
    ):
        object.__setattr__(self, "id", id if id is not None else node_id)
        object.__setattr__(self, "state_vector", state_vector)
        object.__setattr__(self, "parents", parents if parents is not None else parent_ids or set())
        object.__setattr__(self, "transition_rule", transition_rule)
        object.__setattr__(self, "causal_input_hash", causal_input_hash)

    # ---- READ-ONLY COMPATIBILITY ALIASES ----
    @property
    def node_id(self) -> int:
        return self.id

    @property
    def parent_ids(self) -> Set[int]:
        return self.parents
