# Spectrum — Deterministic Measurement Infrastructure

**Value Proposition**: Spectrum provides exact, reproducible fairness metrics using deterministic algorithms and rational arithmetic. Every computation produces bit-identical results across runs, platforms, and time. No randomness, no floating-point imprecision, no surprises.

## Determinism Guarantees

Spectrum guarantees deterministic behavior through:

- **Exact Rational Arithmetic**: All metrics use Python's `Fraction` type, providing exact rational numbers without floating-point errors
- **No Randomness**: Zero use of random number generation or probabilistic algorithms
- **No Time Dependence**: Results never depend on timestamps, system time, or execution timing
- **No Global Mutable State**: Pure functions with no hidden state or side effects
- **Canonical Ordering**: All collections are sorted consistently for deterministic iteration
- **Deterministic Hashing**: Trace hashes use canonical JSON serialization with sorted keys
- **Replayable Traces**: Every computation can be traced and verified for bit-identical replay

## What Spectrum Excludes

Spectrum intentionally **does not** include:

- Floating-point arithmetic (use `Fraction` instead)
- Random sampling or Monte Carlo methods
- Machine learning or statistical inference
- Approximate algorithms
- Time-based caching or memoization
- Network calls or I/O operations during computation
- Non-deterministic hash functions

This is a **measurement** library, not a learning or inference library.

## Installation

```bash
# Clone the repository
git clone https://github.com/AttraQter-Labs/spectrum.git
cd spectrum

# Install in editable mode
pip install -e .

# Install with dev dependencies
pip install -e ".[dev]"
```

## Requirements

- Python >= 3.12

## Usage Examples

### Basic Fairness Metrics

```python
from spectrum.api import (
    demographic_parity_rates,
    demographic_parity_difference,
    demographic_parity_ratio,
    equal_opportunity_difference,
)

# Binary predictions and group labels
predictions = [1, 0, 1, 1, 0, 0, 1, 1]
groups = ["A", "A", "B", "B", "B", "A", "A", "B"]

# Calculate positive rates per group (returns Fractions)
rates = demographic_parity_rates(predictions, groups)
print(rates)  # {'A': Fraction(3, 4), 'B': Fraction(1, 2)}

# Calculate demographic parity difference
dp_diff = demographic_parity_difference(predictions, groups)
print(dp_diff)  # Fraction(1, 4)

# Calculate demographic parity ratio
dp_ratio = demographic_parity_ratio(predictions, groups)
print(dp_ratio)  # Fraction(2, 3)

# Calculate equal opportunity difference (requires true labels)
true_labels = [1, 0, 1, 1, 0, 1, 1, 0]
eo_diff = equal_opportunity_difference(predictions, true_labels, groups)
print(eo_diff)  # Fraction(...)
```

### Deterministic Tracing

```python
from spectrum.api import create_trace, verify_trace, demographic_parity_rates

# Create a trace of a computation
inputs = {"outputs": [1, 0, 1], "groups": ["A", "A", "B"]}
result = demographic_parity_rates([1, 0, 1], ["A", "A", "B"])

trace1 = create_trace("demographic_parity_rates", inputs, result)
print(trace1["hash"])  # SHA-256 hash of canonical trace

# Run the same computation again
result2 = demographic_parity_rates([1, 0, 1], ["A", "A", "B"])
trace2 = create_trace("demographic_parity_rates", inputs, result2)

# Verify bit-identical results
assert verify_trace(trace1, trace2)  # True - identical!
assert result == result2  # Also True
```

### Working with Fractions

```python
from fractions import Fraction

# All metrics return Fraction objects for exact arithmetic
rate = Fraction(3, 4)  # Exactly 0.75, no floating-point error

# Convert to float only when needed for display
print(float(rate))  # 0.75

# Exact comparisons
assert Fraction(1, 2) == Fraction(2, 4)  # True
assert Fraction(1, 3) + Fraction(1, 3) + Fraction(1, 3) == Fraction(1, 1)  # True!
```

## Running Tests

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_determinism.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Copyright (c) 2024 AttraQter Labs
