from typing import List

PRESENTS = [
    "twelve Drummers Drumming",
    "eleven Pipers Piping",
    "ten Lords-a-Leaping",
    "nine Ladies Dancing",
    "eight Maids-a-Milking",
    "seven Swans-a-Swimming",
    "six Geese-a-Laying",
    "five Gold Rings",
    "four Calling Birds",
    "three French Hens",
    "two Turtle Doves",
    "a Partridge in a Pear Tree",
]

DAYS = [
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth",
]


def construct_verse(day: int) -> str:
    last_present = f"and {PRESENTS[-1]}" if day >= 1 else PRESENTS[-1]
    presents = ", ".join(PRESENTS[-day - 1 : -1] + [last_present])
    verse = (
        f"On the {DAYS[day]} day of Christmas "
        f"my true love gave to me: {presents}."
    )
    return verse


def recite(start_verse: int, end_verse: int) -> List[str]:
    return [construct_verse(day) for day in range(start_verse - 1, end_verse)]
