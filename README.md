# Spectrum

[![CI](https://github.com/AttraQter-Labs/spectrum/actions/workflows/ci.yml/badge.svg)](https://github.com/AttraQter-Labs/spectrum/actions/workflows/ci.yml)
[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/11784/badge)](https://www.bestpractices.dev/projects/11784)

## Overview

<<<<<<< HEAD
**Spectrum** is a deterministic, reproducible verification framework designed for
numerical stability, replay validation, and integrity checking of computational systems.
=======
<<<<<<< HEAD
- Exact reproducibility is required
- All behavior must be auditable
- No learning, randomness, or approximation is permitted
>>>>>>> e299c43 (Add core deterministic modules and documentation)

The project prioritizes:
- Deterministic execution
- Replayable verification
- Transparent, auditable CI
- Supply-chain security alignment (OpenSSF)

---

## Determinism & Reproducibility

Spectrum enforces determinism through:
- Fixed Python hash seeds
- Explicit replay modules
- Controlled numerical tolerance testing
- No network dependency during test execution

Every CI run is designed to be **bitwise-repeatable** under identical inputs.

---

## Verification Modules

### Replay Engine
Ensures prior computational traces can be replayed and validated deterministically.

<<<<<<< HEAD
### Numerical Stability
Detects nondeterministic floating-point drift across runs and platforms.

---

## Continuous Integration

All changes are validated via GitHub Actions:
- Clean environment
- Deterministic configuration
- Replay and verification checks
- Required passing status checks before merge

---

## Security & Best Practices

This project aligns with:
- OpenSSF Best Practices
- Principle of least privilege CI permissions
- Reproducible builds philosophy

OpenSSF Project Page:

https://www.bestpractices.dev/projects/11784

---

## Licensing

Apache License 2.0

https://www.apache.org/licenses/LICENSE-2.0

---

## Archival & Citation

Releases are designed to be Zenodo-ready for DOI archival once versioned releases are published.
=======
See `GOVERNANCE.md` for change rules and invariants.
=======
## What Spectrum Is

Spectrum is a **deterministic, bit-reproducible measurement engine** designed for:
- Exact computation with integer and rational arithmetic
- Bit-identical reproducibility across all platforms and executions
- Full audit traceability and replayability
- Cryptographic verification of execution integrity

Spectrum provides pure, deterministic functions that guarantee identical outputs for identical inputs, enabling:
- Compliance auditing
- Financial calculations requiring exact precision
- Scientific computations requiring reproducibility
- Distributed systems requiring consensus

## What Spectrum Is Not

Spectrum is explicitly **NOT**:
- **NOT** machine learning or AI
- **NOT** probabilistic or statistical
- **NOT** predictive or forecasting
- **NOT** adaptive or learning
- **NOT** heuristic or approximate
- **NOT** dependent on floating-point arithmetic
- **NOT** dependent on randomness, time, or environment

Spectrum makes no predictions, learns nothing, and adapts to nothing. It is a pure computational engine.

## Determinism Guarantees

Spectrum provides the following **absolute guarantees**:

1. **Bit-Identical Reproducibility**: Given identical inputs, all executions produce bit-identical outputs
2. **No Randomness**: No random number generation or non-deterministic operations
3. **No Time Dependence**: No system time, clock, or timestamp dependencies
4. **No Environment Dependence**: No environment variables, locale, or platform-specific behavior
5. **Exact Arithmetic**: Only integer and rational (Fraction) arithmetic - no floating-point
6. **Immutable State**: All state objects are immutable
7. **Canonical Ordering**: All collections use deterministic, canonical ordering
8. **Pure Functions**: All core functions are pure with no side effects

These guarantees enable:
- Third-party verification of results
- Forensic replay of historical executions
- Distributed consensus without coordination
- Compliance with regulatory requirements

## Replay & Audit Model

Spectrum's replay and audit model ensures full traceability:

### Replay
- Any computation can be replayed by providing the same input bytes
- `spectrum.replay.run(input_bytes)` produces deterministic output
- Multiple replays always produce bit-identical results
- No execution-order dependencies

### Verification
- `spectrum.verify.verify(input_bytes, claimed_output)` provides cryptographic verification
- Verification recomputes the result and checks bit-for-bit equality
- Third parties can independently verify any claimed result
- No trust required - only mathematics

### Audit Trail
- All executions are deterministic and replayable
- Historical executions can be forensically reconstructed
- Compliance audits can verify claimed results
- No hidden state or non-deterministic behavior

---

## License

Spectrum is licensed under the **MIT License**.

See `LICENSE` for details.
>>>>>>> 3d8db75 (Add core deterministic modules and documentation)
>>>>>>> e299c43 (Add core deterministic modules and documentation)
