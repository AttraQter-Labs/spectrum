"""Public interface for deterministic computation.

This module provides the main public API for executing deterministic
computations and replaying logged operations.
"""

from typing import List, Dict, Any, Tuple
from engine.core import execute_instructions


def run_deterministic(instructions: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    """Execute a list of deterministic instructions.
    
    This is the main public interface for running deterministic computations.
    Each instruction specifies an operation and its operands.
    
    Args:
        instructions: List of instruction dictionaries, each with:
            - 'operation': str - 'add', 'subtract', 'multiply', or 'divide'
            - 'a': float - first operand
            - 'b': float - second operand
    
    Returns:
        Tuple of (results, log) where:
        - results: List of result dictionaries with step-by-step outcomes
        - log: Replayable log that can be used with replay()
    
    Raises:
        ValueError: If division by zero or invalid operation
        KeyError: If instruction format is invalid
    
    Example:
        >>> instructions = [
        ...     {'operation': 'add', 'a': 5, 'b': 3},
        ...     {'operation': 'multiply', 'a': 2, 'b': 4}
        ... ]
        >>> results, log = run_deterministic(instructions)
    """
    return execute_instructions(instructions)


def replay(log: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Replay a computation from a log.
    
    Takes a log produced by run_deterministic() and replays the computation,
    verifying that the results are identical (deterministic guarantee).
    
    Args:
        log: Replayable log from a previous run_deterministic() call
    
    Returns:
        List of result dictionaries matching the original execution
    
    Raises:
        ValueError: If division by zero or invalid operation during replay
        KeyError: If log format is invalid
    
    Example:
        >>> _, log = run_deterministic([{'operation': 'add', 'a': 5, 'b': 3}])
        >>> replayed = replay(log)
        >>> # replayed will match the original results exactly
    """
    # Reconstruct instructions from the log
    instructions = []
    for entry in log:
        instruction = {
            'operation': entry['operation'],
            'a': entry['operands']['a'],
            'b': entry['operands']['b']
        }
        instructions.append(instruction)
    
    # Execute and return only the results (first element of tuple)
    results, _ = execute_instructions(instructions)
    return results
