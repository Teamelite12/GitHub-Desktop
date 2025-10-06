# BUGGY VERSION
# Minimal tests, missing edge cases, no assertions for exceptions.

from calculator import add, divide, sum_list

def test_add():
    assert add(2, 2) == 5  # wrong expectation

def test_div():
    divide(4,0)  # should test zero division

def test_sum():
    assert sum_list([1,2,3]) == 7