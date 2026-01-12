from fractions import Fraction
from spectrum.lattice.node import LatticeNode
from spectrum.invariants.proof import register_proof, run_proofs, list_proofs

def test_proof_registry():
    def always_true(nodes):
        return True

    register_proof("trivial_proof", always_true)

    nodes = [
        LatticeNode(0, (Fraction(0),), set(), None, b""),
    ]

    assert "trivial_proof" in list_proofs()
    assert run_proofs(nodes)
