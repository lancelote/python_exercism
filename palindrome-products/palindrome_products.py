from typing import List, Tuple, Optional, Iterator

Factors = Tuple[int, int]
Report = Tuple[Optional[int], List[Factors]]


def is_palindrome(number: int) -> bool:
    string = str(number)
    return string == string[::-1]


def smallest(max_factor: int, min_factor: int) -> Report:
    return palindrome(min_factor, max_factor)


def largest(max_factor: int, min_factor: int) -> Report:
    return palindrome(min_factor, max_factor, rev=False)


def get_factors(number: int, start: int, stop: int) -> Iterator[Factors]:
    """Yield all possible number factors from a given range."""
    for i in range(start, stop + 1):
        if number % i == 0 and start <= i <= number // i <= stop:
            yield i, number // i


def is_valid_factor(factor: int, number: int, start: int, stop: int) -> bool:
    """Is given factor a valid number factor from a given range?"""
    return number % factor == 0 and start <= number // factor <= stop


def palindrome(start, stop, rev: bool = True) -> Report:
    if start > stop:
        raise ValueError("stop is less than start")

    if rev:
        candidates = range(start ** 2, stop ** 2 + 1)
    else:
        candidates = range(stop ** 2, start ** 2 - 1, -1)

    for candidate in filter(is_palindrome, candidates):
        for factor in range(start, stop + 1):
            if is_valid_factor(factor, candidate, start, stop):
                return candidate, list(get_factors(candidate, start, stop))
    return None, []
