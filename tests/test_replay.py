"""
Test deterministic replay: verify bit-identical outputs across runs.

This test ensures that identical inputs always produce identical outputs,
including identical serialization, hashes, and trace data.
"""

from fractions import Fraction
from spectrum.lattice.node import LatticeNode
from spectrum.serialization.canonical import serialize_nodes, hash_nodes
from spectrum.replay.replay import replay_nodes
import hashlib


def test_replay_deterministic_run():
    """
    Run the same computation twice and verify bit-identical outputs.
    """
    # Define input
    input_data = (
        LatticeNode(id=0, state_vector=(Fraction(0),), parents=set()),
        LatticeNode(id=1, state_vector=(Fraction(1, 2),), parents={0}),
        LatticeNode(id=2, state_vector=(Fraction(3, 4),), parents={0, 1}),
    )
    
    # Run 1
    serialized1 = serialize_nodes(input_data)
    replayed1 = replay_nodes(serialized1)
    hash1 = hash_nodes(replayed1)
    
    # Run 2 (identical input)
    serialized2 = serialize_nodes(input_data)
    replayed2 = replay_nodes(serialized2)
    hash2 = hash_nodes(replayed2)
    
    # Verify bit-identical outputs
    assert serialized1 == serialized2, "Serialization must be deterministic"
    assert replayed1 == replayed2, "Replay must be deterministic"
    assert hash1 == hash2, "Hash must be deterministic"


def test_replay_trace_stability():
    """
    Verify that replay traces are stable across multiple runs.
    """
    nodes = (
        LatticeNode(id=10, state_vector=(Fraction(5, 7),), parents=set()),
        LatticeNode(id=11, state_vector=(Fraction(2, 3),), parents={10}),
    )
    
    # Run multiple times
    traces = []
    for _ in range(3):
        serialized = serialize_nodes(nodes)
        replayed = replay_nodes(serialized)
        trace = tuple(serialized)
        traces.append((trace, replayed))
    
    # All traces must be identical
    assert all(t[0] == traces[0][0] for t in traces)
    assert all(t[1] == traces[0][1] for t in traces)


def test_replay_hash_bit_identical():
    """
    Verify that output hashes are bit-identical across runs.
    This is the core determinism guarantee.
    """
    input_nodes = (
        LatticeNode(id=100, state_vector=(Fraction(1),), parents=set()),
        LatticeNode(id=101, state_vector=(Fraction(2),), parents={100}),
        LatticeNode(id=102, state_vector=(Fraction(3),), parents={100, 101}),
    )
    
    # Compute hash multiple times
    hashes = []
    for run in range(10):
        h = hash_nodes(input_nodes)
        hashes.append(h)
    
    # All hashes must be identical
    first_hash = hashes[0]
    assert all(h == first_hash for h in hashes), "Hashes must be bit-identical"
    
    # Verify hash is stable string
    assert isinstance(first_hash, str)
    assert len(first_hash) == 64  # SHA-256 hex digest


def test_replay_ordering_canonical():
    """
    Verify that node ordering is canonical regardless of input order.
    """
    # Same nodes, different input order
    nodes_order1 = (
        LatticeNode(id=2, state_vector=(Fraction(3),), parents={1}),
        LatticeNode(id=0, state_vector=(Fraction(1),), parents=set()),
        LatticeNode(id=1, state_vector=(Fraction(2),), parents={0}),
    )
    
    nodes_order2 = (
        LatticeNode(id=0, state_vector=(Fraction(1),), parents=set()),
        LatticeNode(id=1, state_vector=(Fraction(2),), parents={0}),
        LatticeNode(id=2, state_vector=(Fraction(3),), parents={1}),
    )
    
    # Both should produce identical canonical serialization
    hash1 = hash_nodes(nodes_order1)
    hash2 = hash_nodes(nodes_order2)
    
    assert hash1 == hash2, "Canonical ordering must be deterministic"


def test_replay_output_verification():
    """
    Test the core replay verification pattern: run -> serialize -> replay -> verify.
    """
    # Original computation
    original = (
        LatticeNode(id=0, state_vector=(Fraction(7, 11),), parents=set()),
    )
    
    # Serialize
    serialized = serialize_nodes(original)
    output_hash = hash_nodes(original)
    
    # Replay from serialized form
    replayed = replay_nodes(serialized)
    replayed_hash = hash_nodes(replayed)
    
    # Verification: replayed output matches original
    assert replayed == original
    assert replayed_hash == output_hash
    
    # This is the core guarantee: given serialized input,
    # replay produces bit-identical output
    assert serialized == serialize_nodes(replayed)
