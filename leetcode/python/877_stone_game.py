from typing import List


class Solution:

    def stoneGame(self, piles: List[int]) -> bool:
        N = len(piles)
        dp = {(i, i): val for i, val in enumerate(piles)}
        for size in range(1, N):
            for i in range(N-size):
                begin = piles[i] - dp[(i+1, i+size)]
                end = piles[i+size] - dp[(i, i+size-1)]
                dp[(i, i+size)] = max(begin, end)
        return dp[(0, N-1)] > 0
