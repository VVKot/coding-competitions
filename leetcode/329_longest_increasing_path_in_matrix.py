from typing import List


class Solution:

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        self.M = matrix
        self.y = len(matrix)
        self.x = len(matrix[0])
        self.dp = [[-1 for _ in range(self.x)] for _ in range(self.y)]
        result = 0
        for i in range(self.y):
            for j in range(self.x):
                curr = self.dfs(i, j)
                result = max(result, curr)
        return result

    def dfs(self, i: int, j: int) -> int:
        if self.dp[i][j] > -1:
            return self.dp[i][j]
        result = 1
        for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            y, x = i + dy, j + dx
            if not (0 <= y < self.y and 0 <= x < self.x):
                continue
            if self.M[y][x] <= self.M[i][j]:
                continue
            self.dp[y][x] = self.dfs(y, x)
            result = max(result, self.dp[y][x] + 1)
        return result
