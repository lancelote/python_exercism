def is_isogram(string: str) -> bool:
    seen = set()
    for char in string.lower():
        if char.isalpha():
            if char in seen:
                return False
            else:
                seen.add(char)
    return True
