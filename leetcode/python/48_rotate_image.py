from typing import List


class Solution:

    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()
        N = len(matrix)
        for y in range(N):
            for x in range(y):
                matrix[y][x], matrix[x][y] = matrix[x][y], matrix[y][x]
