from typing import List


def equilateral(sides: List[float]) -> bool:
    unique_sides = set(sides)
    return len(unique_sides) == 1 and unique_sides != {0}


def isosceles(sides):
    pass


def scalene(sides):
    pass
