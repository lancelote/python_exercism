from random import sample
from string import ascii_uppercase
from itertools import product
from typing import Generator


class Robot:
    available_names: Generator[str, None, None] = (
        "".join(x)
        for x in product(
            sample(ascii_uppercase, 26),
            sample(ascii_uppercase, 26),
            sample([str(x).zfill(3) for x in range(1000)], 1000),
        )
    )

    def __init__(self) -> None:
        self.name: str = next(self.available_names)

    def reset(self) -> None:
        self.name = next(self.available_names)
