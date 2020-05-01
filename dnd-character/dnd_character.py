import random


ABILITIES = [
    "strength",
    "dexterity",
    "constitution",
    "intelligence",
    "wisdom",
    "charisma",
]


def modifier(constitution: int) -> int:
    return round((constitution - 10) / 2 - 0.1)


class Character:
    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int

    def __init__(self) -> None:
        for ability in ABILITIES:
            setattr(self, ability, self.generate_stat())

    @staticmethod
    def generate_stat() -> int:
        throws = [random.randint(1, 6) for _ in range(4)]
        return sum(throws) - min(throws)

    def ability(self) -> int:
        return getattr(self, random.choice(ABILITIES))

    @property
    def hitpoints(self) -> int:
        return 10 + modifier(self.constitution)
