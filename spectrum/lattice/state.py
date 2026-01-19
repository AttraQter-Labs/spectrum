from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True)
class LatticeState:
    """Lightweight stub for lattice states."""
    value: Any
