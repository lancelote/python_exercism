def square_of_sum(number: int) -> int:
    return ((1 + number) * number // 2) ** 2


def sum_of_squares(number: int) -> int:
    return number * (number + 1) * (2 * number + 1) // 6


def difference_of_squares(number: int) -> int:
    return abs(sum_of_squares(number) - square_of_sum(number))
