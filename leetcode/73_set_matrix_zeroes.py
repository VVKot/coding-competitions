from typing import List


class Solution:

    def setZeroes(self, matrix: List[List[int]]) -> None:
        H = len(matrix)
        W = len(matrix[0])
        col1 = 1
        for y in range(H):
            for x in range(W):
                if not matrix[y][x]:
                    if x == 0:
                        col1 = 0
                    else:
                        matrix[0][x] = matrix[y][0] = 0
        for y in reversed(range(H)):
            for x in reversed(range(W)):
                if x == 0:
                    if col1 == 0:
                        matrix[y][x] = 0
                elif matrix[0][x] == 0 or matrix[y][0] == 0:
                    matrix[y][x] = 0
