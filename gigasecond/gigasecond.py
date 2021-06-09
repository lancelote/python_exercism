from datetime import datetime
from datetime import timedelta


def add(moment: datetime) -> datetime:
    return moment + timedelta(seconds=10 ** 9)
