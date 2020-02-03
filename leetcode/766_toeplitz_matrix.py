from typing import List


class Solution:

    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for y, row in enumerate(matrix):
            for x, curr in enumerate(row):
                if y != 0 and x != 0:
                    prev = matrix[y-1][x-1]
                    if prev != curr:
                        return False
        return True
