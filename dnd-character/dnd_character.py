import random
from dataclasses import dataclass, fields
from functools import cached_property


def modifier(constitution: int) -> int:
    return round((constitution - 10) / 2 - 0.1)


@dataclass
class Character:
    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int

    def __init__(self) -> None:
        for field in fields(self):
            setattr(self, field.name, self.generate_stat())

    @staticmethod
    def generate_stat() -> int:
        throws = [random.randint(1, 6) for _ in range(4)]
        return sum(throws) - min(throws)

    def ability(self) -> int:
        field_names = [field.name for field in fields(self)]
        return getattr(self, random.choice(field_names))

    @cached_property
    def hitpoints(self) -> int:
        return 10 + modifier(self.constitution)
