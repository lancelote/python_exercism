import re

PATTERN = r"^1?([2-9][0-9]{2})([2-9][0-9]{2})([0-9]{4})$"


class PhoneNumber:
    def __init__(self, number: str) -> None:
        number = "".join(x for x in number if x.isalnum())

        if match := re.match(PATTERN, number):
            self.area_code, self.exchange, self.subscriber = match.groups()
        else:
            raise ValueError("wrong format")

        self.number = f"{self.area_code}{self.exchange}{self.subscriber}"

    def pretty(self) -> str:
        return f"({self.area_code}) {self.exchange}-{self.subscriber}"
