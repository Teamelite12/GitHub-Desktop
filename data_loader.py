# FIXED VERSION
"""
Data loading helpers.

Improvements:
- Context manager for JSON (no leak).
- Reduced memory use (stream lines).
- Removed unreachable code.
- Added validation + docstrings.
"""

import json
from typing import Iterator, Any

def load_json(path: str) -> Any:
    with open(path, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in {path}: {e}") from e

def iter_nonempty_lines(path: str) -> Iterator[str]:
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            s = line.strip()
            if s:
                yield s

This is a change
