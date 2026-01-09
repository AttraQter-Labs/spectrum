"""Deterministic computation engine.

This module provides pure deterministic functions for arithmetic operations
and instruction execution with no global state, randomness, or time dependence.
"""

from engine.core import add, subtract, multiply, divide, execute_instructions

__all__ = ["add", "subtract", "multiply", "divide", "execute_instructions"]
