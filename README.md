# Spectrum

[![CI](https://github.com/AttraQter-Labs/spectrum/actions/workflows/ci.yml/badge.svg)](https://github.com/AttraQter-Labs/spectrum/actions/workflows/ci.yml)
[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/11784/badge)](https://www.bestpractices.dev/projects/11784)

## Overview

**Spectrum** is a deterministic, reproducible verification framework designed for
numerical stability, replay validation, and integrity checking of computational systems.

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
