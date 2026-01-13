# Spectrum — Security Model

Spectrum is secured by **determinism**, not secrecy.

## Threat Model
Spectrum assumes:
- Adversarial inputs
- Malicious execution environments
- Full visibility of source code

## Defenses
- No hidden state
- No stochastic behavior
- No model weights
- No training data
- No runtime mutation

Security is achieved by:
- Mathematical invariants
- Deterministic state transitions
- Immutable execution semantics

## Non-Goals
Spectrum does not attempt to:
- Obfuscate logic
- Hide implementation
- Prevent reverse engineering

Correctness is provable, not concealed.

