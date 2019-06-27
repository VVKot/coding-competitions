from typing import List


class Solution:

    def setZeroes(self, matrix: List[List[int]]) -> None:
        H = len(matrix)
        W = len(matrix[0])
        rows = [1] * H
        cols = [1] * W
        for y in range(H):
            for x in range(W):
                if not matrix[y][x]:
                    rows[y] = 0
                    cols[x] = 0
        for y in range(H):
            for x in range(W):
                if not rows[y] or not cols[x]:
                    matrix[y][x] = 0
