from typing import List


class Matrix:
    def __init__(self, matrix_string: str) -> None:
        self.matrix = [
            [int(item) for item in line.split()]
            for line in matrix_string.split("\n")
        ]

    def row(self, index: int) -> List[int]:
        return self.matrix[index - 1].copy()

    def column(self, index: int) -> List[int]:
        return [line[index - 1] for line in self.matrix]
