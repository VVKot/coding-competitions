"""
T: O(N**2)
S: O(N**2)

Simple DP solution, we skip two characters if they are the same, and add on of
them if they are not. To find the optimal solution, in case of inequality we
consider both cases.
"""

from functools import lru_cache


class Solution:

    def minInsertions(self, s: str) -> int:

        @lru_cache(None)
        def dp(i, j):
            if i >= j:
                return 0
            elif s[i] == s[j]:
                return dp(i + 1, j - 1)
            else:
                return min(dp(i, j - 1), dp(i + 1, j)) + 1

        return dp(0, len(s) - 1)
