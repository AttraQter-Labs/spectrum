# Spectrum Determinism Contract

Any consumer of Spectrum MUST adhere to the following:

1. Inputs must be explicit, finite, and serializable
2. Outputs must be replayable and verifiable
3. No hidden state, clocks, randomness, or learning
4. Identical inputs MUST produce bit-identical outputs

Violations void correctness guarantees.

This contract is binding.
