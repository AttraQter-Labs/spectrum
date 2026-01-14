#!/usr/bin/env python3
"""
Deterministic Replay Proof for Spectrum Engine

This script demonstrates bit-identical reproducibility by:
1. Creating a deterministic computation using existing engine components
2. Logging every intermediate state
3. Computing final output hash and full trace hash (SHA-256)

Running this script twice MUST yield identical output and hash values.
Any deviation indicates non-determinism or implementation error.

No external dependencies beyond standard library and spectrum itself.
No randomness, no time, no environment access, no floating point.
"""

import sys
import hashlib
from fractions import Fraction
from spectrum.lattice.node import LatticeNode
from spectrum.serialization.canonical import serialize_nodes, hash_nodes
from spectrum.replay.replay import replay_nodes


def log_state(label: str, value: str) -> None:
    """Log intermediate state to stdout."""
    print(f"[STATE] {label}: {value}")


def compute_deterministic_lattice():
    """
    Create a deterministic lattice computation.
    
    This uses rational arithmetic (Fraction) and canonical ordering
    to ensure bit-identical reproducibility.
    """
    log_state("START", "Creating deterministic lattice nodes")
    
    # Create a sequence of deterministic lattice nodes
    # Using exact rational arithmetic only
    nodes = []
    
    # Root node
    node0 = LatticeNode(
        id=0,
        state_vector=(Fraction(0, 1),),
        parents=set()
    )
    nodes.append(node0)
    log_state("NODE_0", f"id={node0.id}, state={node0.state_vector}")
    
    # First generation - deterministic rational increments
    node1 = LatticeNode(
        id=1,
        state_vector=(Fraction(1, 2),),
        parents={0}
    )
    nodes.append(node1)
    log_state("NODE_1", f"id={node1.id}, state={node1.state_vector}, parents={sorted(node1.parents)}")
    
    node2 = LatticeNode(
        id=2,
        state_vector=(Fraction(3, 4),),
        parents={0}
    )
    nodes.append(node2)
    log_state("NODE_2", f"id={node2.id}, state={node2.state_vector}, parents={sorted(node2.parents)}")
    
    # Second generation - merge paths
    node3 = LatticeNode(
        id=3,
        state_vector=(Fraction(5, 8),),
        parents={1, 2}
    )
    nodes.append(node3)
    log_state("NODE_3", f"id={node3.id}, state={node3.state_vector}, parents={sorted(node3.parents)}")
    
    # Third generation - complex rational state
    node4 = LatticeNode(
        id=4,
        state_vector=(Fraction(7, 16), Fraction(11, 32)),
        parents={3}
    )
    nodes.append(node4)
    log_state("NODE_4", f"id={node4.id}, state={node4.state_vector}, parents={sorted(node4.parents)}")
    
    # Additional nodes for non-trivial computation
    node5 = LatticeNode(
        id=5,
        state_vector=(Fraction(13, 32), Fraction(17, 64)),
        parents={4}
    )
    nodes.append(node5)
    log_state("NODE_5", f"id={node5.id}, state={node5.state_vector}, parents={sorted(node5.parents)}")
    
    node6 = LatticeNode(
        id=6,
        state_vector=(Fraction(19, 64), Fraction(23, 128)),
        parents={4}
    )
    nodes.append(node6)
    log_state("NODE_6", f"id={node6.id}, state={node6.state_vector}, parents={sorted(node6.parents)}")
    
    # Final convergence node
    node7 = LatticeNode(
        id=7,
        state_vector=(Fraction(29, 128), Fraction(31, 256)),
        parents={5, 6}
    )
    nodes.append(node7)
    log_state("NODE_7", f"id={node7.id}, state={node7.state_vector}, parents={sorted(node7.parents)}")
    
    # Convert to tuple for immutability
    nodes_tuple = tuple(nodes)
    log_state("TOTAL_NODES", str(len(nodes_tuple)))
    
    return nodes_tuple


def compute_trace_hash(nodes):
    """
    Compute hash of the entire computation trace.
    
    This includes all intermediate states in canonical order.
    """
    log_state("TRACE_HASH_START", "Computing trace hash from all states")
    
    h = hashlib.sha256()
    
    # Hash each node in canonical order (by id)
    for node in sorted(nodes, key=lambda n: n.id):
        # Create deterministic representation
        node_repr = f"id={node.id}|"
        node_repr += f"state={','.join(f'{f.numerator}/{f.denominator}' for f in node.state_vector)}|"
        node_repr += f"parents={','.join(str(p) for p in sorted(node.parents))}"
        
        h.update(node_repr.encode('utf-8'))
        h.update(b'\n')
        
        log_state(f"TRACE_HASH_NODE_{node.id}", node_repr)
    
    trace_hash = h.hexdigest()
    log_state("TRACE_HASH_COMPLETE", trace_hash)
    
    return trace_hash


def main():
    """Main proof execution."""
    print("=" * 70)
    print("Spectrum Deterministic Replay Proof")
    print("=" * 70)
    
    # Step 1: Create deterministic lattice
    print("\n--- Step 1: Creating Deterministic Lattice ---")
    nodes = compute_deterministic_lattice()
    
    # Step 2: Serialize to canonical form
    print("\n--- Step 2: Canonical Serialization ---")
    log_state("SERIALIZE_START", "Converting nodes to canonical form")
    serialized = serialize_nodes(nodes)
    for i, line in enumerate(serialized):
        log_state(f"SERIALIZED_{i}", line)
    log_state("SERIALIZE_COMPLETE", f"Generated {len(serialized)} canonical lines")
    
    # Step 3: Compute node hash (using existing engine function)
    print("\n--- Step 3: Computing Output Hash ---")
    output_hash = hash_nodes(nodes)
    log_state("OUTPUT_HASH", output_hash)
    
    # Step 4: Replay nodes (round-trip verification)
    print("\n--- Step 4: Replay Verification ---")
    log_state("REPLAY_START", "Reconstructing nodes from serialization")
    replayed = replay_nodes(serialized)
    log_state("REPLAY_COMPLETE", f"Reconstructed {len(replayed)} nodes")
    
    # Verify replay matches original
    if nodes == replayed:
        log_state("REPLAY_MATCH", "SUCCESS - Original and replayed nodes are identical")
    else:
        log_state("REPLAY_MATCH", "FAILURE - Mismatch detected!")
        sys.exit(1)
    
    # Step 5: Compute trace hash (all intermediate states)
    print("\n--- Step 5: Computing Trace Hash ---")
    trace_hash = compute_trace_hash(nodes)
    
    # Step 6: Final output
    print("\n" + "=" * 70)
    print("PROOF COMPLETE")
    print("=" * 70)
    print(f"OUTPUT_HASH: {output_hash}")
    print(f"TRACE_HASH:  {trace_hash}")
    print("=" * 70)
    print("\nAny deviation in these hashes across runs indicates non-determinism.")
    print("Both hashes MUST be identical on every execution with Python 3.10+.")
    print("=" * 70)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
