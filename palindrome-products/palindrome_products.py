from typing import List, Tuple, Optional, Generator

Factors = Tuple[int, int]


def is_palindrome(number: int) -> bool:
    string = str(number)
    return string == string[::-1]


def smallest(max_factor: int, min_factor: int) -> Tuple[Optional[int], List[Factors]]:
    return palindrome(min_factor, max_factor)


def largest(max_factor: int, min_factor: int) -> Tuple[Optional[int], List[Factors]]:
    return palindrome(min_factor, max_factor, rev=False)


def get_factors(number: int, min_factor: int, max_factor: int) -> Generator[Tuple[int, int], None, None]:
    for i in range(min_factor, max_factor + 1):
        if number % i == 0 and min_factor <= i <= number // i <= max_factor:
            yield i, number // i


def palindrome(min_factor, max_factor, rev: bool = True) -> Tuple[Optional[int], List[Factors]]:
    if min_factor > max_factor:
        raise ValueError("min factor can't be greater than max factor")

    if rev:
        candidates = range(min_factor ** 2, max_factor ** 2 + 1)
    else:
        candidates = range(max_factor ** 2, min_factor ** 2 - 1, -1)

    for candidate in candidates:
        if is_palindrome(candidate):
            for factor in range(min_factor, max_factor + 1):
                if candidate % factor == 0 and min_factor <= candidate // factor <= max_factor:
                    return candidate, list(get_factors(candidate, min_factor, max_factor))
    return None, []
