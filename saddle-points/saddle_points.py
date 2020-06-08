from typing import List, Dict


def saddle_points(matrix: List[List[int]]) -> List[Dict[str, int]]:
    """Find all saddle points in matrix.

    Saddle point is

    - greater than or equal to every element in its row
    - and less than or equal to every element in its column.
    """
    points: List[Dict[str, int]] = []

    try:
        for i, row in enumerate(matrix):
            for j, item in enumerate(row):
                if max(row) == item & min(row[j] for row in matrix) == item:
                    points.append({"row": i + 1, "column": j + 1})
        return points
    except IndexError:
        raise ValueError("irregular matrix")
