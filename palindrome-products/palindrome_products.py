from typing import Iterator
from typing import List
from typing import Optional
from typing import Tuple

Factors = Tuple[int, int]
Report = Tuple[Optional[int], List[Factors]]


def is_palindrome(num: int) -> bool:
    string = str(num)
    return string == string[::-1]


def smallest(max_factor: int, min_factor: int) -> Report:
    return palindrome(min_factor, max_factor)


def largest(max_factor: int, min_factor: int) -> Report:
    return palindrome(min_factor, max_factor, reverse=False)


def get_factors(num: int, start: int, stop: int) -> Iterator[Factors]:
    """Yield all possible number pair factors from a given range."""
    for factor in range(start, stop + 1):
        if num % factor == 0 and start <= factor <= num // factor <= stop:
            yield factor, num // factor


def is_valid_factor(factor: int, num: int, start: int, stop: int) -> bool:
    """Is given factor a valid number factor from a given range?"""
    return num % factor == 0 and start <= num // factor <= stop


def palindrome(start, stop, reverse: bool = True) -> Report:
    if start > stop:
        raise ValueError("stop is less than start")

    if reverse:
        candidates = range(start ** 2, stop ** 2 + 1)
    else:
        candidates = range(stop ** 2, start ** 2 - 1, -1)

    for candidate in filter(is_palindrome, candidates):
        for factor in range(start, stop + 1):
            if is_valid_factor(factor, candidate, start, stop):
                return candidate, list(get_factors(candidate, start, stop))
    return None, []
