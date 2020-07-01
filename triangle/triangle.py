from typing import List


def is_valid(triangle: List[float]) -> bool:
    """Sides are not 0 and the longest one is less than the sum of others."""
    return set(triangle) != {0} and sum(triangle) > max(triangle) * 2


def equilateral(triangle: List[float]) -> bool:
    """All sides of an equal length."""
    return len(set(triangle)) == 1 and is_valid(triangle)


def isosceles(triangle: List[float]) -> bool:
    """At least two sides of the equal length."""
    return len(set(triangle)) <= 2 and is_valid(triangle)


def scalene(triangle: List[float]) -> bool:
    """All sides of a different length."""
    return len(set(triangle)) == 3 and is_valid(triangle)


def degenerate(triangle: List[float]) -> bool:
    """Has zero area."""
    return sum(triangle) == 2 * max(triangle)
