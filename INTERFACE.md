# Spectrum – Public Interface Contract

This document defines the **only supported interface surface** for Spectrum.

Anything not explicitly listed here is **internal** and **unstable**.

## Guarantees
- Deterministic
- Bit-identical execution
- No randomness
- No learning
- No time, environment, or floating-point dependence

## Allowed Dependencies
- Python standard library (deterministic subsets only)
- Integer and rational arithmetic only

## Stable Interface
The following are the ONLY stability guarantees:

- Pure functions
- Explicit inputs
- Explicit outputs
- No hidden state
- No side effects

## Prohibited
- Floating point arithmetic
- Randomness of any kind
- Time, clock, or environment access
- Global mutable state
- Learning, adaptation, or heuristics

## Versioning
Breaking changes increment the **major** version.
Internal changes do NOT imply compatibility.

This contract is enforced beginning at tag:
v3.0-interface-boundary
