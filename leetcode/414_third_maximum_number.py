from typing import List


class Solution:

    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        return nums[-3] if len(nums) >= 3 else nums[-1]
