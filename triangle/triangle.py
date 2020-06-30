from typing import List


def equilateral(sides: List[float]) -> bool:
    sides = set(sides)
    return len(sides) == 1 and sides != {0}


def isosceles(sides):
    pass


def scalene(sides):
    pass
