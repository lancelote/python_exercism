import functools
from typing import Dict
from typing import List


class Allergies:

    allergens: Dict[str, int] = {
        "eggs": 1,
        "peanuts": 2,
        "shellfish": 4,
        "strawberries": 8,
        "tomatoes": 16,
        "chocolate": 32,
        "pollen": 64,
        "cats": 128,
    }

    def __init__(self, score: int) -> None:
        self.score = score

    def allergic_to(self, allergen: str) -> bool:
        return bool(self.score & self.allergens[allergen])

    @functools.cached_property
    def lst(self) -> List[str]:
        return [
            allergen
            for allergen, score in self.allergens.items()
            if score & self.score
        ]
