def classify(number: int) -> str:
    if number <= 0:
        raise ValueError(f"{number} is not a natural number")

    aliquot_sum = sum(x for x in range(1, number // 2 + 1) if number % x == 0)

    if aliquot_sum == number:
        category = "perfect"
    elif aliquot_sum > number:
        category = "abundant"
    else:
        category = "deficient"

    return category
