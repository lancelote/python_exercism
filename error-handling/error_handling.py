from typing import Optional
from typing import Tuple

Result = Tuple[bool, Optional[int]]


def handle_error_by_throwing_exception() -> None:
    raise ValueError("unexpected value")


def handle_error_by_returning_none(input_data: str) -> Optional[int]:
    try:
        return int(input_data)
    except ValueError:
        return None


def handle_error_by_returning_tuple(input_data: str) -> Result:
    result = handle_error_by_returning_none(input_data)
    return result is not None, result


def filelike_objects_are_closed_on_exception(filelike_object) -> None:
    with filelike_object as file:
        file.do_something()
