# FIXED VERSION
"""
Simple in-memory feature flag store.

Improvements:
- Added get with default False (no KeyError).
- Added list + batch set feature (new feature).
- Reduced duplication (tech debt).
- Added type hints & docstrings.
"""

from typing import Dict, Iterable

_flags: Dict[str, bool] = {}

def set_flag(name: str, value: bool) -> None:
    _flags[name] = value

def enable(name: str) -> None:
    set_flag(name, True)

def disable(name: str) -> None:
    set_flag(name, False)

def is_enabled(name: str) -> bool:
    return _flags.get(name, False)

def toggle(name: str) -> bool:
    new_val = not is_enabled(name)
    set_flag(name, new_val)
    return new_val

def batch_set(pairs: Iterable[tuple[str, bool]]) -> None:
    for k, v in pairs:
        set_flag(k, v)

def list_flags() -> Dict[str, bool]:
    return dict(_flags)

A Change
