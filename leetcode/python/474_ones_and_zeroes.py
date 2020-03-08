from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for s in strs:
            zeros = s.count('0')
            ones = s.count('1')
            for y in range(m, zeros - 1, -1):
                for x in range(n, ones - 1, -1):
                    dp[y][x] = max(dp[y][x], 1 + dp[y - zeros][x - ones])
        return dp[m][n]
