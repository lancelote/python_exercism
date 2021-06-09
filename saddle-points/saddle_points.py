from typing import Dict
from typing import List


def saddle_points(matrix: List[List[int]]) -> List[Dict[str, int]]:
    """Find all saddle points in matrix.

    Saddle point is

    - greater than or equal to every element in its row
    - and less than or equal to every element in its column.
    """
    points: List[Dict[str, int]] = []

    row_max = [max(row) for row in matrix]
    col_mins = [min(col) for col in zip(*matrix)]

    try:
        for i, row in enumerate(matrix):
            for j, item in enumerate(row):
                if row_max[i] == item & col_mins[j] == item:
                    points.append({"row": i + 1, "column": j + 1})
        return points
    except IndexError:
        raise ValueError("irregular matrix")
