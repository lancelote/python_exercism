from operator import gt, lt
from functools import partial
from typing import Iterable, List, Dict, Callable


CompareFn = Callable[[int, int], bool]


def get_ids(items: Iterable[int], comp: CompareFn) -> List[int]:
    ids = []
    base_value = None

    for i, value in enumerate(items):
        if base_value is None or comp(value, base_value):
            base_value = value
            ids = [i]
        elif value == base_value:
            ids.append(i)

    return ids


get_min_ids = partial(get_ids, comp=lt)
get_max_ids = partial(get_ids, comp=gt)


def saddle_points(matrix: List[List[int]]) -> List[Dict[str, int]]:
    points = []

    for row in matrix:
        min_col_ids = get_max_ids(row)
        for col_id in min_col_ids:
            min_row_ids = get_min_ids(row[col_id] for row in matrix)
            for row_id in min_row_ids:
                points.append({"row": row_id, "column": col_id})

    return points
