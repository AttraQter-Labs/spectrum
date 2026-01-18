mkdir -p spectrum/lattice
cat > spectrum/lattice/state.py <<'PY'
"""
Basic lattice state stub for testing.
"""

from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True)
class LatticeState:
    """Placeholder for lattice state representation."""
    value: Any
PY
