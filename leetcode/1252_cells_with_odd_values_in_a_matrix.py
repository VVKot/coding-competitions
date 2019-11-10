"""
T: O(N*M + (N+M)*L)
S: O(N*M)

A simple simulation solution which follows instructions.
"""


from typing import List


class Solution:

    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        cells = [[0 for _ in range(m)] for _ in range(n)]
        for i, j in indices:
            for x in range(m):
                cells[i][x] ^= 1
            for y in range(n):
                cells[y][j] ^= 1
        return sum(val for row in cells for val in row)
