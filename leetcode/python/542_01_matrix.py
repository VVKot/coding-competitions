from typing import List


class Solution:

    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        matrix = [[10000 * x for x in row] for row in matrix]
        for _ in range(4):
            for row in matrix:
                for j in range(1, len(row)):
                    row[j] = min(row[j], row[j-1] + 1)
            matrix = list(map(list, zip(*matrix[::-1])))
        return matrix
