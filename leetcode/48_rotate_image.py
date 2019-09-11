from typing import List


class Solution:

    def rotate(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        for x in range(cols):
            for y in range(rows//2):
                matrix[y][x], matrix[rows-1-y][x] = \
                    matrix[rows-1-y][x], matrix[y][x]
        for y in range(rows):
            for x in range(y+1, cols):
                matrix[y][x], matrix[x][y] = matrix[x][y], matrix[y][x]
