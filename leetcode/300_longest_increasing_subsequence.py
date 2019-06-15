from typing import List


class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        N = len(nums)
        dp = [1] * N
        for i in range(1, N):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
