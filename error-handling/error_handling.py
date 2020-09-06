from typing import Optional, Tuple


def handle_error_by_throwing_exception() -> None:
    raise ValueError("unexpected value")


def handle_error_by_returning_none(input_data: str) -> Optional[int]:
    try:
        return int(input_data)
    except ValueError:
        return None


def handle_error_by_returning_tuple(
    input_data: str,
) -> Tuple[bool, Optional[int]]:
    try:
        return True, int(input_data)
    except ValueError:
        return False, None


def filelike_objects_are_closed_on_exception(filelike_object) -> None:
    try:
        filelike_object.open()
        filelike_object.do_something()
    except Exception as e:
        raise e
    finally:
        filelike_object.close()
