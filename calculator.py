"""Calculator utilities with safer operations and convenience helpers."""

from __future__ import annotations

from math import sqrt
from typing import Iterable


Number = float | int


def add(a: Number, b: Number) -> Number:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """Return the difference between two numbers."""
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """Return the product of two numbers."""
    return a * b


def divide(a: Number, b: Number) -> float:
    """Return a divided by b.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def power(base: Number, exponent: Number) -> Number:
    """Return base raised to exponent."""
    return base**exponent


def modulus(a: Number, b: Number) -> Number:
    """Return the remainder when a is divided by b.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot calculate modulus with zero.")
    return a % b


def square_root(value: Number) -> float:
    """Return the square root of a non-negative number.

    Raises:
        ValueError: If value is negative.
    """
    if value < 0:
        raise ValueError("Cannot take the square root of a negative number.")
    return sqrt(value)


def average(numbers: Iterable[Number]) -> float:
    """Return the arithmetic mean of the given numbers.

    Raises:
        ValueError: If numbers is empty.
    """
    values = list(numbers)
    if not values:
        raise ValueError("Cannot calculate the average of an empty list.")
    return sum(values) / len(values)


def sum_list(numbers: Iterable[Number]) -> Number:
    """Return the sum of all numbers in the iterable."""
    return sum(numbers)
