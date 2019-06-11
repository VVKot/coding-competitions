from typing import List


class Solution:

    def sortColors(self, nums: List[int]) -> None:
        zero = one = 0
        for i, num in enumerate(nums):
            nums[i] = 2
            if num < 2:
                nums[one] = 1
                one += 1
            if num == 0:
                nums[zero] = 0
                zero += 1
