import heapq
from typing import List


class Solution:

    def thirdMax(self, nums: List[int]) -> int:
        max_nums = []
        for num in set(nums):
            if len(max_nums) < 3:
                heapq.heappush(max_nums, num)
            else:
                heapq.heappushpop(max_nums, num)
        return max_nums[0] if len(max_nums) == 3 else max(max_nums)
