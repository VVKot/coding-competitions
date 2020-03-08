import bisect
from typing import List


class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        increasing = [(float('inf'))] * (N + 1)
        for num in nums:
            index = bisect.bisect_left(increasing, num)
            increasing[index] = num
        return increasing.index(float('inf'))
