import math


def score(x: float, y: float) -> int:
    distance = math.sqrt(x * x + y * y)
    points = 0

    if distance <= 1:
        points = 10
    elif distance <= 5:
        points = 5
    elif distance <= 10:
        points = 1

    return points
