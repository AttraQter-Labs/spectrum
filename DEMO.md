# Canonical Demo - Deterministic Replay Verification

This demo showcases Spectrum's core deterministic guarantee: **identical inputs produce bit-identical outputs, every time**.

## Running the Demo

```bash
python demo.py
```

## What It Does

The demo demonstrates the complete deterministic computation and replay cycle:

### Step 1: Create Deterministic Input
Creates lattice nodes with exact rational arithmetic (using Python's `Fraction` type):
- Node 0: state=(1/1), no parents
- Node 1: state=(1/2, 3/4), parent={0}
- Node 2: state=(2/3, 5/7), parents={0, 1}

### Step 2: Canonical Serialization
Serializes nodes to a canonical text form that is:
- Order-independent (sorted by node ID)
- Platform-independent
- Stable across Python versions

### Step 3: Compute Deterministic Hash
Computes a SHA-256 hash of the canonical serialization.

**Expected Hash:** `7579a53bbc1ea72f2f4e462a26b439e0e571565781128dca419e290fc93c9e0a`

This hash will be **identical** on:
- Every run on the same machine
- Every run on different machines
- Every run on different operating systems
- Every run now and forever

### Step 4: Replay from Serialization
Reconstructs the lattice nodes from their serialized form.

### Step 5: Verification
Verifies that:
- Original hash == Replayed hash (bit-identical)
- Original nodes == Replayed nodes (structurally identical)

## Replay Steps

To manually replay the demo computation:

1. **Serialize**: Convert nodes to canonical form
   ```python
   from spectrum.serialization.canonical import serialize_nodes
   serialized = serialize_nodes(nodes)
   ```

2. **Replay**: Reconstruct from serialization
   ```python
   from spectrum.replay.replay import replay_nodes
   replayed = replay_nodes(serialized)
   ```

3. **Verify**: Check bit-identical hash
   ```python
   from spectrum.serialization.canonical import hash_nodes
   assert hash_nodes(nodes) == hash_nodes(replayed)
   ```

## Deterministic Properties

This demo proves:

✅ **Bit-identical reproducibility** - Same output hash every run  
✅ **Full replayability** - Can reconstruct from serialized form  
✅ **Auditor-verifiable** - Third parties can verify the computation  
✅ **No randomness** - No random number generation  
✅ **No time dependence** - No clock or timestamp usage  
✅ **No environment dependence** - No environment variable access  
✅ **Exact arithmetic** - Rational numbers, not floating point  

## Testing Determinism

Run the demo multiple times and verify identical output:

```bash
python demo.py > run1.txt
python demo.py > run2.txt
diff run1.txt run2.txt
# Should produce no output (files are identical)
```

## Implementation Details

- **Language**: Pure Python 3.12+
- **Arithmetic**: `fractions.Fraction` (exact rational arithmetic)
- **Hashing**: SHA-256 (cryptographically stable)
- **Serialization**: Custom canonical format (see `spectrum/serialization/canonical.py`)
- **Replay**: Deterministic parser (see `spectrum/replay/replay.py`)

## Non-Features (By Design)

The demo does NOT use:
- ❌ Floating point arithmetic
- ❌ Random number generation
- ❌ Time/clock functions
- ❌ Environment variables
- ❌ Machine learning
- ❌ Probabilistic algorithms
- ❌ Heuristics or approximations

These are deliberately excluded to maintain determinism.
