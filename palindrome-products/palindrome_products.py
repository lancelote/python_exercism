from itertools import combinations


def is_palindrome(number: int) -> bool:
    string = str(number)
    return string == string[::-1]


def palindromes(min_factor, max_factor):
    for x, y in combinations(range(min_factor, max_factor + 1), 2):
        candidate = x * y
        if is_palindrome(candidate):
            yield (candidate, [x, y])


def largest(min_factor, max_factor) -> int:
    return max(palindromes(min_factor, max_factor))


def smallest(min_factor, max_factor):
    return min(palindromes(min_factor, max_factor))
