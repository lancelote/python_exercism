import re


def all_capitals(phrase: str) -> bool:
    return bool(
        not re.search(r"[a-z]", phrase) and re.search(r"[A-Z]", phrase)
    )


def is_nothing(hey_bob: str) -> bool:
    return len(hey_bob) == 0


def response(hey_bob: str) -> str:
    phrase = hey_bob.strip()

    if is_nothing(phrase):
        return "Fine. Be that way!"
    if all_capitals(phrase):
        if phrase.endswith("?"):
            return "Calm down, I know what I'm doing!"
        else:
            return "Whoa, chill out!"
    elif phrase.endswith("?"):
        return "Sure."
    else:
        return "Whatever."
