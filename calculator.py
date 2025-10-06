# BUGGY VERSION
def add(a, b):
    return a - b  # bug: should be addition

def divide(a, b):
    return a / b  # no zero check

def sum_list(nums):
    total = 0
    for n in nums:
        total += n
    return total

# prints on import (bad practice)
print("Loaded calc")