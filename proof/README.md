# Deterministic Proof Artifacts

This directory contains proof artifacts demonstrating Spectrum's deterministic guarantees.

## Purpose

These artifacts prove that Spectrum produces bit-identical results across executions.
This is critical for:
- Third-party verification
- Audit compliance
- Deterministic computation guarantees
- Reproducibility validation

## Files

### `replay_proof.py`
Executable proof script that:
1. Creates a non-trivial deterministic computation using Spectrum's lattice engine
2. Logs every intermediate state to stdout
3. Computes two SHA-256 hashes:
   - **OUTPUT_HASH**: Hash of final serialized lattice state
   - **TRACE_HASH**: Hash of complete execution trace

Running this script multiple times MUST produce identical hash values.

### `hash_proof.txt`
Certification document containing:
- Input description
- Exact command to reproduce
- Expected OUTPUT_HASH value
- Expected TRACE_HASH value
- Certification statement

Any deviation from documented hash values indicates non-determinism or implementation error.

### `README.md` (this file)
Instructions for third-party verification.

## Third-Party Verification Instructions

### Prerequisites
- Python 3.10 or higher
- Git

### Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AttraQter-Labs/spectrum.git
   cd spectrum
   ```

2. **Install Spectrum:**
   ```bash
   pip install -e .
   ```

3. **Run the proof (first execution):**
   ```bash
   python3 proof/replay_proof.py
   ```
   
   Note the final OUTPUT_HASH and TRACE_HASH values.

4. **Run the proof again (second execution):**
   ```bash
   python3 proof/replay_proof.py
   ```
   
   The OUTPUT_HASH and TRACE_HASH MUST be identical to the first run.

5. **Verify against certification:**
   ```bash
   cat proof/hash_proof.txt
   ```
   
   Compare your hash values against the documented expected values.

### Success Criteria

✅ **SUCCESS** if:
- First and second runs produce identical OUTPUT_HASH
- First and second runs produce identical TRACE_HASH
- Both hashes match values in `hash_proof.txt`

❌ **FAILURE** if:
- Hash values differ between runs
- Hash values differ from `hash_proof.txt`
- Script produces errors or non-deterministic output

### Understanding the Proof

The proof demonstrates determinism by:
1. Using only exact rational arithmetic (Python Fraction type)
2. Maintaining canonical ordering of all data structures
3. Avoiding randomness, time, environment, and floating point
4. Serializing intermediate states in a canonical format
5. Computing cryptographic hashes over complete execution traces

The lattice computation includes:
- 8 nodes in a directed acyclic graph (DAG)
- Multiple merge points (nodes with multiple parents)
- Multi-dimensional rational state vectors
- Canonical serialization and replay

## Implementation Details

### No External Dependencies
The proof uses only:
- Python standard library
- Spectrum's existing engine components

No new dependencies are introduced.

### Deterministic Guarantees
- **Exact arithmetic**: All computations use Fraction (rational numbers)
- **Canonical ordering**: All collections sorted deterministically
- **Immutable state**: All nodes are frozen dataclasses
- **No side effects**: Pure functional transformations
- **Hash stability**: SHA-256 over canonical serialization

### CI Integration

The CI pipeline (`.github/workflows/ci.yml`) automatically:
1. Runs `replay_proof.py` twice
2. Extracts OUTPUT_HASH from both runs
3. Asserts they are identical
4. Fails the build on any mismatch

This ensures every commit maintains deterministic guarantees.

## Notes

- This proof does NOT benchmark performance
- This proof does NOT make claims about speed or efficiency
- This proof ONLY demonstrates bit-identical reproducibility
- The computation is non-trivial but purposely kept small for fast CI execution

## License

See repository LICENSE file. Spectrum is commercial software by AttraQtor-Labs LLC.
