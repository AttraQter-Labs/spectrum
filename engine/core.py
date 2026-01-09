"""Core deterministic computation functions.

All functions in this module are pure and deterministic:
- No global state
- No randomness
- No time dependence
- Identical inputs always produce identical outputs
"""

from typing import List, Dict, Any, Tuple


def add(a: float, b: float) -> float:
    """Add two numbers deterministically.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        Sum of a and b
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract two numbers deterministically.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        Difference of a and b (a - b)
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers deterministically.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        Product of a and b
    """
    return a * b


def divide(a: float, b: float) -> float:
    """Divide two numbers deterministically with safe error handling.
    
    Args:
        a: Numerator
        b: Denominator
    
    Returns:
        Quotient of a and b (a / b)
    
    Raises:
        ValueError: If b is zero (division by zero)
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b


def execute_instructions(instructions: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    """Execute a list of arithmetic instructions deterministically.
    
    Each instruction is a dictionary with:
    - 'operation': str - one of 'add', 'subtract', 'multiply', 'divide'
    - 'a': float - first operand
    - 'b': float - second operand
    
    Args:
        instructions: List of instruction dictionaries
    
    Returns:
        Tuple of (results, log) where:
        - results: List of result dictionaries with 'step', 'operation', 'operands', 'result'
        - log: Copy of results for replay purposes (replayable log)
    
    Raises:
        ValueError: If division by zero is attempted
        KeyError: If instruction format is invalid
    """
    operations = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }
    
    results = []
    
    for step, instruction in enumerate(instructions):
        operation_name = instruction['operation']
        a = instruction['a']
        b = instruction['b']
        
        if operation_name not in operations:
            raise ValueError(f"Unknown operation: {operation_name}")
        
        operation_func = operations[operation_name]
        result = operation_func(a, b)
        
        result_entry = {
            'step': step,
            'operation': operation_name,
            'operands': {'a': a, 'b': b},
            'result': result
        }
        results.append(result_entry)
    
    # Create a deep copy for the log to ensure it's independent
    log = [dict(entry) for entry in results]
    for entry in log:
        entry['operands'] = dict(entry['operands'])
    
    return results, log
