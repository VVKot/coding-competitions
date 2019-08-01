from typing import List


class Solution:

    def maxProfit(self, nums: List[int]) -> int:
        if not nums:
            return 0
        N = len(nums)
        dp = [0] * N
        for i in reversed(range(N-1)):
            max_profit = 0
            for j in range(i+1, N):
                curr_profit = 0
                if nums[j] > nums[i]:
                    curr_profit += nums[j] - nums[i]
                    next_profit = dp[j+2] if j < N-2 else 0
                    curr_profit += next_profit
                else:
                    curr_profit = dp[j]
                max_profit = max(max_profit, curr_profit)
            dp[i] = max(dp[i], max_profit)
        return dp[0]
