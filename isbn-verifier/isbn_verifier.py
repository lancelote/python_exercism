VALID = set("0123456789X")


def is_valid(isbn: str) -> bool:
    items = [x for x in isbn if x in VALID]

    if len(items) != 10:
        return False

    if items[-1] == "X":
        items[-1] = "10"

    try:
        total = sum(int(item) * (10 - i) for (i, item) in enumerate(items))
    except ValueError:
        return False

    return total % 11 == 0
