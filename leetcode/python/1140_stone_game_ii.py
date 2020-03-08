from typing import List
from functools import lru_cache


class Solution:

    def stoneGameII(self, piles: List[int]) -> int:
        N = len(piles)
        prefix_sum = self.get_prefix_sum(piles)

        @lru_cache(None)
        def get_diff(start, m):
            if start >= N:
                return 0
            max_score = float('-inf')
            stones_left = min(2*m+1, N-start+1)
            for i in range(1, stones_left):
                next_score = get_diff(start+i, max(m, i))
                curr_score = prefix_sum[start+i] - prefix_sum[start]
                max_score = max(max_score, curr_score - next_score)
            return max_score

        max_diff = get_diff(0, 1)
        return (sum(piles) + max_diff) // 2

    def get_prefix_sum(self, nums: List[int]):
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)
        return prefix_sum
