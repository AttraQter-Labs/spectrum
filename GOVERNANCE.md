# Spectrum Governance

Owner: **AttraQtor-Labs LLC**

## Core Invariants (Non-Negotiable)

The following properties MUST always hold:

- Determinism
- Bit-identical reproducibility
- No randomness
- No floating-point dependence
- No time, environment, or network dependence
- No learning or adaptive behavior

## Change Policy

Allowed:
- Documentation improvements
- Deterministic refactors that preserve behavior
- Additional tests that strengthen guarantees

Disallowed:
- Introducing randomness, time, or entropy
- Floating-point arithmetic
- Nondeterministic ordering
- Weakening or skipping tests
- Network calls or external state dependence

## Versioning

Once a release tag is marked **stable**, it is considered immutable.

Breaking changes require:
- Explicit major version bump
- Formal review
- Determinism re-verification

## Enforcement

These rules are enforced by:
- CI workflows
- Determinism checks
- Human review as final gate

Violation of these rules invalidates the release.

## Status

**Governed. Protected. Immutable by default.**
