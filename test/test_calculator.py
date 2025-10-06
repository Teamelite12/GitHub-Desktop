# FIXED VERSION
"""
Improved test coverage:
- Correct expectations.
- Tests error path.
- Parametrized style (manual loop to stay simple).
"""

from calculator import add, divide, sum_list
import pytest

def test_add():
    cases = [(2, 2, 4), (5, -2, 3), (0, 0, 0)]
    for a, b, exp in cases:
        assert add(a, b) == exp

def test_divide_normal():
    assert divide(8, 2) == 4

def test_divide_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

def test_sum_list():
    assert sum_list([1, 2, 3, 4]) == 10
    assert sum_list([]) == 0