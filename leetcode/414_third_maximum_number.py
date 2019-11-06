import heapq
from typing import List


class Solution:

    def thirdMax(self, nums: List[int]) -> int:
        return heapq.nlargest(3, set(nums))[-1] if len(nums) >= 3 \
            else max(nums)
