from functools import wraps
from typing import List, Callable

CheckFunction = Callable[[List[float]], bool]


def is_valid(func: CheckFunction) -> CheckFunction:
    """Sides are not 0 and the longest one is less than the sum of others."""

    @wraps(func)
    def wrapper(triangle: List[float]) -> bool:
        valid = set(triangle) != {0} and sum(triangle) > max(triangle) * 2
        return valid and func(triangle)

    return wrapper


@is_valid
def equilateral(triangle: List[float]) -> bool:
    """All sides of an equal length."""
    return len(set(triangle)) == 1


@is_valid
def isosceles(triangle: List[float]) -> bool:
    """At least two sides of the equal length."""
    return len(set(triangle)) <= 2


@is_valid
def scalene(triangle: List[float]) -> bool:
    """All sides of a different length."""
    return len(set(triangle)) == 3


def degenerate(triangle: List[float]) -> bool:
    """Has zero area."""
    return sum(triangle) == 2 * max(triangle)
