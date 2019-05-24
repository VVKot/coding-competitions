from typing import List, Tuple


class NumMatrix:

    def __init__(self, matrix: List[List[int]]) -> None:
        self.M = self.get_prepared_matrix(matrix)

    def get_prepared_matrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not any(matrix):
            return matrix
        rows = len(matrix)
        cols = len(matrix[0])
        for y in range(rows):
            for x in range(cols):
                top, left, top_left = self.get_near_cell(matrix, y, x)
                matrix[y][x] += top + left - top_left
        return matrix

    def get_near_cell(self,
                      matrix: List[List[int]],
                      y: int,
                      x: int) -> Tuple[int, int, int]:
        top = matrix[y-1][x] if y else 0
        left = matrix[y][x-1] if x else 0
        top_left = matrix[y-1][x-1] if y and x else 0
        return top, left, top_left

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        top, left, top_left = self.get_near_square(row1, col1, row2, col2)
        return self.M[row2][col2] - top - left + top_left

    def get_near_square(self,
                        y1: int,
                        x1: int,
                        y2: int,
                        x2: int) -> Tuple[int, int, int]:
        top = self.M[y1-1][x2] if y1 else 0
        left = self.M[y2][x1-1] if x1 else 0
        top_left = self.M[y1-1][x1-1] if y1 and x1 else 0
        return top, left, top_left
