from typing import List


class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        N = len(A)
        for i in range(1, N):
            for j in range(N):
                A[i][j] += self.get_top_row_min(A, i-1, j)
        return min(A[-1])

    def get_top_row_min(self, A: List[List[int]], i: int, j: int) -> int:
        N = len(A)
        left = 0 if not j else j-1
        right = N-1 if j == N-1 else j + 1
        return min(A[i][left:right+1])
