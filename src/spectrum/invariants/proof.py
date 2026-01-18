from typing import Iterable, Callable, Dict
from spectrum.lattice.node import LatticeNode

Proof = Callable[[Iterable[LatticeNode]], bool]

_PROOFS: Dict[str, Proof] = {}

def register_proof(name: str, proof: Proof) -> None:
    """
    Register a deterministic proof obligation.
    """
    if name in _PROOFS:
        raise ValueError(f"Proof '{name}' already registered")
    _PROOFS[name] = proof

def run_proofs(nodes: Iterable[LatticeNode]) -> bool:
    """
    All registered proofs must pass.
    """
    for name, proof in _PROOFS.items():
        if not proof(nodes):
            return False
    return True

def list_proofs():
    return tuple(_PROOFS.keys())
