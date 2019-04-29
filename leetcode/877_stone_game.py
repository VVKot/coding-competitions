from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        N = len(piles)
        dp = piles[:]
        for right in range(1, N):
            for left in range(N-right):
                dp[right] = max(dp[left] - dp[left+1],
                                dp[right+left] - dp[left])
        return dp[0] > 0
