# Spectrum — Deterministic Computation Engine

A pure deterministic computation engine with guaranteed reproducibility. All operations are deterministic with no global state, randomness, or time dependence.

## Purpose

Spectrum provides a minimal, deterministic computation engine for arithmetic operations with the following guarantees:
- **Determinism**: Identical inputs always produce identical outputs
- **Bit-identical reproducibility**: Results are exactly reproducible across runs
- **No randomness**: No use of random number generators
- **No time dependence**: No timestamps or time-based functions
- **No global state**: All functions are pure with explicit inputs/outputs
- **Safe operations**: Division by zero raises ValueError deterministically
- **Replayability**: All computations can be replayed from logs

## Installation

```bash
pip install -e .
```

For development:
```bash
pip install -e ".[dev]"
```

## Usage

### Basic Operations

```python
from engine.core import add, subtract, multiply, divide

# All operations are deterministic
result = add(5, 3)        # 8
result = subtract(10, 4)  # 6
result = multiply(3, 7)   # 21
result = divide(20, 4)    # 5.0

# Division by zero raises ValueError
try:
    result = divide(10, 0)
except ValueError as e:
    print(e)  # "Division by zero is not allowed"
```

### Instruction Execution

```python
from api.public import run_deterministic, replay

# Define a sequence of operations
instructions = [
    {'operation': 'add', 'a': 10, 'b': 5},
    {'operation': 'multiply', 'a': 3, 'b': 4},
    {'operation': 'divide', 'a': 100, 'b': 4}
]

# Execute instructions
results, log = run_deterministic(instructions)

# Results contain step-by-step outcomes
for result in results:
    print(f"Step {result['step']}: {result['operation']} -> {result['result']}")

# Replay from log (produces identical results)
replayed_results = replay(log)
assert replayed_results == results  # Always True
```

### Determinism Guarantees

```python
# Same inputs always produce same outputs
results1, log1 = run_deterministic(instructions)
results2, log2 = run_deterministic(instructions)
assert results1 == results2
assert log1 == log2

# Replay is deterministic
replay1 = replay(log1)
replay2 = replay(log1)
assert replay1 == replay2
```

## Testing

Run the test suite:

```bash
pytest
```

Run with verbose output:

```bash
pytest -v
```

## Architecture

```
spectrum/
├── engine/
│   ├── __init__.py      # Engine module exports
│   └── core.py          # Pure deterministic functions
├── api/
│   ├── __init__.py      # API module exports
│   └── public.py        # Public interface (run_deterministic, replay)
├── tests/
│   └── test_engine.py   # Comprehensive test suite
├── README.md            # This file
├── LICENSE              # MIT License
└── pyproject.toml       # Python package configuration
```

## Determinism Guarantees

Spectrum guarantees deterministic behavior through:

1. **Pure Functions**: All operations are pure functions with no side effects
2. **No Global State**: No global variables or shared mutable state
3. **No Randomness**: No use of `random` module or non-deterministic sources
4. **No Time Dependence**: No use of `time`, `datetime`, or system clock
5. **Explicit Inputs**: All inputs are explicitly passed as function arguments
6. **Immutable Operations**: Operations do not modify input data
7. **Deterministic Errors**: Even errors (like division by zero) are deterministic

## License

MIT License - see LICENSE file for details.
