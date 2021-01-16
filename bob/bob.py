def response(hey_bob: str) -> str:
    phrase = hey_bob.strip()

    if len(phrase) == 0:
        return "Fine. Be that way!"
    if phrase.isupper():
        if phrase.endswith("?"):
            return "Calm down, I know what I'm doing!"
        else:
            return "Whoa, chill out!"
    elif phrase.endswith("?"):
        return "Sure."
    else:
        return "Whatever."
