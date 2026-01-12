"""Public API for Spectrum - Deterministic Measurement Infrastructure.

This module provides the stable public API with deterministic guarantees.
All functions are deterministic, reproducible, and produce bit-identical results.
"""

from typing import Any, Dict, List, Tuple
from fractions import Fraction
import json
import hashlib

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
    "create_trace",
    "verify_trace",
]


def create_trace(function_name: str, inputs: Dict[str, Any], 
                 outputs: Any) -> Dict[str, Any]:
    """Create a deterministic trace of a function call.
    
    The trace includes a canonical hash of the inputs and outputs,
    allowing for replay verification and ensuring bit-identical results.
    
    Args:
        function_name: Name of the function being traced
        inputs: Dictionary of input parameters (must be JSON-serializable)
        outputs: Function output (must be JSON-serializable or Fraction)
        
    Returns:
        Dictionary containing the trace with canonical hash
    """
    # Convert Fractions to strings for deterministic serialization
    serialized_inputs = _serialize_for_trace(inputs)
    serialized_outputs = _serialize_for_trace(outputs)
    
    # Create canonical JSON (sorted keys, no whitespace)
    trace_data = {
        "function": function_name,
        "inputs": serialized_inputs,
        "outputs": serialized_outputs,
    }
    
    canonical_json = json.dumps(trace_data, sort_keys=True, separators=(',', ':'))
    trace_hash = hashlib.sha256(canonical_json.encode('utf-8')).hexdigest()
    
    return {
        "function": function_name,
        "inputs": serialized_inputs,
        "outputs": serialized_outputs,
        "hash": trace_hash,
    }


def verify_trace(trace1: Dict[str, Any], trace2: Dict[str, Any]) -> bool:
    """Verify that two traces are bit-identically equal.
    
    Args:
        trace1: First trace dictionary
        trace2: Second trace dictionary
        
    Returns:
        True if traces are identical, False otherwise
    """
    return trace1.get("hash") == trace2.get("hash")


def _serialize_for_trace(obj: Any) -> Any:
    """Serialize objects for deterministic tracing.
    
    Converts Fractions to strings and ensures sorted dictionaries.
    """
    if isinstance(obj, Fraction):
        return f"{obj.numerator}/{obj.denominator}"
    elif isinstance(obj, dict):
        return {k: _serialize_for_trace(v) for k in sorted(obj.keys())}
    elif isinstance(obj, (list, tuple)):
        return [_serialize_for_trace(item) for item in obj]
    else:
        return obj
