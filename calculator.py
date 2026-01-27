# FIXED VERSION
"""
Calculator utilities.

Improvements:
- Fixed add bug.
- Safe divide with ZeroDivisionError handling.
- Added type hints.
- Removed side-effect print.
"""

from typing import Iterable

def add(a: float, b: float) -> float:
    return a + b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("b must not be zero")
    return a / b

def sum_list(nums: Iterable[float]) -> float:
    return sum(nums)
A Change
