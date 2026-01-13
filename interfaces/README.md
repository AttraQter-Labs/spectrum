# Spectrum Interfaces

This directory defines **public, stable interfaces** for interacting with the Spectrum core.

Rules:
- Interfaces may evolve, core semantics may NOT
- Interfaces must be deterministic adapters only
- No randomness, time, IO, or environment dependence

Any interface violating determinism is invalid.

The core is authoritative.
