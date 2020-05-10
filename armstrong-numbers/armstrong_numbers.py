def is_armstrong_number(number: int) -> bool:
    return number == sum(int(x) ** len(str(number)) for x in str(number))
