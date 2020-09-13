MATCH = {
    "}": "{",
    "]": "[",
    ")": "(",
}

OPEN = set("{[(")
CLOSE = set("}])")


def is_paired(input_string: str) -> bool:
    stack = []
    for char in input_string:
        if char in OPEN:
            stack.append(char)
        elif char in CLOSE:
            if not stack or MATCH[char] != stack.pop():
                return False
        else:
            pass
    return not stack
