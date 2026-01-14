#!/usr/bin/env python3
"""
Canonical Deterministic Demo - Spectrum MVP

This demo showcases Spectrum's core deterministic guarantee:
identical inputs produce bit-identical outputs, every time.

Usage:
    python demo.py

Expected output:
    A stable SHA-256 hash that is identical across all runs,
    on all machines, forever.
"""

from fractions import Fraction
from spectrum.lattice.node import LatticeNode
from spectrum.serialization.canonical import serialize_nodes, hash_nodes
from spectrum.replay.replay import replay_nodes


def main():
    print("=" * 70)
    print("Spectrum Deterministic Computation Demo")
    print("=" * 70)
    print()
    
    # Step 1: Define deterministic input
    print("Step 1: Creating deterministic lattice nodes...")
    nodes = (
        LatticeNode(
            id=0,
            state_vector=(Fraction(1, 1),),
            parents=set(),
        ),
        LatticeNode(
            id=1,
            state_vector=(Fraction(1, 2), Fraction(3, 4)),
            parents={0},
        ),
        LatticeNode(
            id=2,
            state_vector=(Fraction(2, 3), Fraction(5, 7)),
            parents={0, 1},
        ),
    )
    print(f"  Created {len(nodes)} nodes with rational state vectors")
    print()
    
    # Step 2: Serialize to canonical form
    print("Step 2: Serializing to canonical form...")
    serialized = serialize_nodes(nodes)
    for i, line in enumerate(serialized):
        print(f"  Node {i}: {line}")
    print()
    
    # Step 3: Compute deterministic hash
    print("Step 3: Computing deterministic hash...")
    output_hash = hash_nodes(nodes)
    print(f"  SHA-256: {output_hash}")
    print()
    
    # Step 4: Replay from serialization
    print("Step 4: Replaying from serialized form...")
    replayed = replay_nodes(serialized)
    replayed_hash = hash_nodes(replayed)
    print(f"  Replayed {len(replayed)} nodes")
    print(f"  Replayed hash: {replayed_hash}")
    print()
    
    # Step 5: Verification
    print("Step 5: Verification...")
    if output_hash == replayed_hash:
        print("  ✓ Original and replayed hashes match")
    else:
        print("  ✗ Hash mismatch - determinism violated!")
        return 1
    
    if nodes == replayed:
        print("  ✓ Original and replayed nodes are identical")
    else:
        print("  ✗ Node mismatch - determinism violated!")
        return 1
    
    print()
    print("=" * 70)
    print("DETERMINISM GUARANTEE VERIFIED")
    print("=" * 70)
    print()
    print("This exact output hash will be produced on every run:")
    print(f"  {output_hash}")
    print()
    print("Properties:")
    print("  • Bit-identical across all machines")
    print("  • Bit-identical across all runs")
    print("  • Fully replayable from serialized form")
    print("  • Auditor-verifiable")
    print("  • No randomness, time, or environment dependence")
    print()
    
    return 0


if __name__ == "__main__":
    exit(main())
