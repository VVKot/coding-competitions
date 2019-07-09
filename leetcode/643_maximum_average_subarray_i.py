from typing import List


class Solution:

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = max_sum = sum(nums[:k])
        n = len(nums)
        for i in range(0, n-k):
            curr_sum -= nums[i]
            curr_sum += nums[i+k]
            max_sum = max(max_sum, curr_sum)
        return max_sum / k
