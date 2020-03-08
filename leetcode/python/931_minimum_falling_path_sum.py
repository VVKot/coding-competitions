"""
T: O(N**2)
S: O(1)

On each step, find what's the minimum sum to get to the previous step. Add this
sum to the current one. In the end, the minimum sum in the last row is our
target sum.
"""

from typing import List


class Solution:

    def minFallingPathSum(self, A: List[List[int]]) -> int:
        N = len(A)
        for i in range(1, N):
            for j in range(N):
                A[i][j] += self.get_row_min(A, i - 1, j)
        return min(A[-1])

    def get_row_min(self, A: List[List[int]], i: int, j: int) -> int:
        N = len(A)
        left = 0 if j == 0 else j - 1
        right = N - 1 if j == N - 1 else j + 1
        return min(A[i][left:right + 1])
