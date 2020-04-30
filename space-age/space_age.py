from enum import Enum
from functools import partialmethod as pm

BASE = 31557600  # Earth orbital period in seconds


class Period(Enum):
    EARTH = BASE
    MERCURY = BASE * 0.2408467
    VENUS = BASE * 0.61519726
    MARS = BASE * 1.8808158
    JUPITER = BASE * 11.862615
    SATURN = BASE * 29.447498
    URANUS = BASE * 84.016846
    NEPTUNE = BASE * 164.79132


class SpaceAge:
    def __init__(self, seconds: int) -> None:
        self.seconds = seconds

    def on_planet(self, period: Period) -> float:
        return round(self.seconds / period.value, 2)

    on_earth = pm(on_planet, period=Period.EARTH)
    on_mercury = pm(on_planet, period=Period.MERCURY)
    on_venus = pm(on_planet, period=Period.VENUS)
    on_mars = pm(on_planet, period=Period.MARS)
    on_jupiter = pm(on_planet, period=Period.JUPITER)
    on_saturn = pm(on_planet, period=Period.SATURN)
    on_uranus = pm(on_planet, period=Period.URANUS)
    on_neptune = pm(on_planet, period=Period.NEPTUNE)
