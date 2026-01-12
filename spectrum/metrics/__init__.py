"""Fairness metrics with exact rational arithmetic."""

from spectrum.metrics.fairness import (
    demographic_parity_rates,
    demographic_parity_difference,
    demographic_parity_ratio,
    equal_opportunity_difference,
)

__all__ = [
    "demographic_parity_rates",
    "demographic_parity_difference",
    "demographic_parity_ratio",
    "equal_opportunity_difference",
]
