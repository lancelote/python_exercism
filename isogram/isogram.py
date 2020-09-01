def is_isogram(string: str) -> bool:
    seen = set()
    for char in string:
        lower_char = char.lower()
        if lower_char.isalnum():
            if lower_char in seen:
                return False
            else:
                seen.add(lower_char)
    return True
