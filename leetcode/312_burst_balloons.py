from typing import List


class Solution:

    def maxCoins(self, nums: List[int]) -> int:
        N = len(nums) + 2
        dp = [[0 for _ in range(N)] for _ in range(N)]
        nums = [1] + nums + [1]
        for step in range(2, N):
            for left in range(N - step):
                right = left + step
                for i in range(left + 1, right):
                    val = nums[left] * nums[i] * nums[right]
                    val += dp[left][i] + dp[i][right]
                    dp[left][right] = max(dp[left][right], val)
        return dp[0][N - 1]
