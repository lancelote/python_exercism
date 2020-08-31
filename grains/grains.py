def square(number: int) -> int:
    if number <= 0 or number > 64:
        raise ValueError("1 <= x < 65 value is allowed")

    return 1 << (number - 1)


def total() -> int:
    return (1 << 64) - 1
