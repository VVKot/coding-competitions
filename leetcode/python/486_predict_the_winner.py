from typing import List


class Solution:

    def PredictTheWinner(self, nums: List[int]) -> bool:
        N = len(nums)
        dp = [0] * N
        for start in range(N, -1, -1):
            for end in range(start+1, N):
                with_start = nums[start] - dp[end]
                with_end = nums[end] - dp[end-1]
                dp[end] = max(with_start, with_end)
        return dp[-1] >= 0
