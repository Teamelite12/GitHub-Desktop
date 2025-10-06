# BUGGY VERSION
# Tries to implement a simple in-memory feature flag store but has logic errors.

_flags = {}

def enable(name):
    _flags[name] = True

def disable(name):
    _flags[name] = False

def is_enabled(name):
    return _flags[name]  # KeyError if missing

def toggle(name):
    if _flags[name] == True:
        _flags[name] = False
    else:
        _flags[name] = True