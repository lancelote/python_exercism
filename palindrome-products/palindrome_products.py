from itertools import combinations_with_replacement as cwr
from typing import NamedTuple, List, Tuple, Optional

Factors = List[int]
Result = Tuple[Optional[int], List[Factors]]


class Candidate(NamedTuple):
    value: int
    factors: Factors


def is_palindrome(number: int) -> bool:
    string = str(number)
    return string == string[::-1]


def palindromes(min_factor: int, max_factor: int) -> List[Candidate]:
    return [
        Candidate(candidate, [x, y])
        for x, y in cwr(range(min_factor, max_factor + 1), 2)
        if is_palindrome(candidate := x * y)
    ]


def largest(min_factor: int, max_factor: int) -> Result:
    return get_palindrome(min_factor, max_factor, max)


def smallest(min_factor: int, max_factor: int) -> Result:
    return get_palindrome(min_factor, max_factor, min)


def get_palindrome(min_factor, max_factor, compare) -> Result:
    if min_factor > max_factor:
        raise ValueError(f"min factor {min_factor} > max factor {max_factor}")
    candidates = palindromes(min_factor, max_factor)
    if not candidates:
        return None, []
    key_value = compare(candidates).value
    key_factors = [
        candidate.factors
        for candidate in candidates
        if candidate.value == key_value
    ]
    return key_value, key_factors
