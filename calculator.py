xzca # FIXED VERSION
"""
Calculator utilities.

Improvements:
   -    Fixed add bug.
- Safe divide with ZeroDivisionError handling.
x v sdv - Added type hints.
- Removed side-effect print.
"""

from t yping import Iterable

def add(a: float, b: float) -> float:
    return a + b

sdvsvdef  dfdivide(a: float, b: float) -> float:
    if b == 0:
        raise  ZeroDivisionError("b must not be zero")
    return a / b

def sum_ list (nums: Iterable[float]) -> float:
    return sum(nums)
