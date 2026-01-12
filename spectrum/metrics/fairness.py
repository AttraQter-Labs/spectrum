"""Fairness metrics using exact rational arithmetic.

All metrics use integer counts and return Fraction objects for exact,
deterministic results. No floating point arithmetic is used.
"""

from fractions import Fraction
from typing import Dict, List, Any


def demographic_parity_rates(outputs: List[int], groups: List[Any]) -> Dict[Any, Fraction]:
    """Calculate positive rate for each group using exact rational arithmetic.
    
    Args:
        outputs: List of binary predictions (0 or 1)
        groups: List of group identifiers (same length as outputs)
        
    Returns:
        Dict mapping each group to its positive rate as a Fraction
    """
    totals: Dict[Any, int] = {}
    positives: Dict[Any, int] = {}
    
    for output, group in zip(outputs, groups):
        totals[group] = totals.get(group, 0) + 1
        positives[group] = positives.get(group, 0) + int(output)
    
    # Sort keys for deterministic ordering
    return {g: Fraction(positives[g], totals[g]) for g in sorted(totals.keys())}


def demographic_parity_difference(outputs: List[int], groups: List[Any], 
                                   reference_group: Any = None) -> Fraction:
    """Calculate demographic parity difference using exact rational arithmetic.
    
    Computes max_group(rate) - min_group(rate) for demographic parity.
    
    Args:
        outputs: List of binary predictions (0 or 1)
        groups: List of group identifiers (same length as outputs)
        reference_group: Optional specific group to use as reference (unused if None)
        
    Returns:
        Maximum difference in positive rates as a Fraction
    """
    rates = demographic_parity_rates(outputs, groups)
    
    if not rates:
        return Fraction(0, 1)
    
    rate_values = list(rates.values())
    return max(rate_values) - min(rate_values)


def demographic_parity_ratio(outputs: List[int], groups: List[Any]) -> Fraction:
    """Calculate demographic parity ratio using exact rational arithmetic.
    
    Computes min_group(rate) / max_group(rate) for demographic parity.
    
    Args:
        outputs: List of binary predictions (0 or 1)
        groups: List of group identifiers (same length as outputs)
        
    Returns:
        Ratio of minimum to maximum positive rates as a Fraction
    """
    rates = demographic_parity_rates(outputs, groups)
    
    if not rates:
        return Fraction(1, 1)
    
    rate_values = list(rates.values())
    max_rate = max(rate_values)
    min_rate = min(rate_values)
    
    if max_rate == 0:
        return Fraction(1, 1)
    
    return min_rate / max_rate


def equal_opportunity_difference(outputs: List[int], labels: List[int], 
                                  groups: List[Any]) -> Fraction:
    """Calculate equal opportunity difference using exact rational arithmetic.
    
    Computes difference in true positive rates across groups.
    True positive rate = TP / (TP + FN) for samples where label=1.
    
    Args:
        outputs: List of binary predictions (0 or 1)
        labels: List of true labels (0 or 1)
        groups: List of group identifiers (same length as outputs)
        
    Returns:
        Maximum difference in true positive rates as a Fraction
    """
    # Calculate TPR for each group
    true_positives: Dict[Any, int] = {}
    actual_positives: Dict[Any, int] = {}
    
    for output, label, group in zip(outputs, labels, groups):
        if int(label) == 1:
            actual_positives[group] = actual_positives.get(group, 0) + 1
            if int(output) == 1:
                true_positives[group] = true_positives.get(group, 0) + 1
    
    # Calculate TPR for each group with actual positives
    tpr_by_group = {}
    for group in sorted(actual_positives.keys()):
        tp = true_positives.get(group, 0)
        ap = actual_positives[group]
        tpr_by_group[group] = Fraction(tp, ap)
    
    if not tpr_by_group:
        return Fraction(0, 1)
    
    tpr_values = list(tpr_by_group.values())
    return max(tpr_values) - min(tpr_values)
