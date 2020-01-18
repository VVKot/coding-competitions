"""
T: O(N)
S: O(1)

A solution without swapping which utilizes a fact that this problem does not
require to swap object by their key, just numbers. In that case, we can count
the last position of zeroes and ones, and insert the numbers at appropriate
positions. We insert two by default so we don't need a counter for it.
"""

from typing import List


class Solution:

    def sortColors(self, nums: List[int]) -> None:
        zero_pointer = one_pointer = 0
        for i, num in enumerate(nums):
            nums[i] = 2
            if num < 2:
                nums[one_pointer] = 1
                one_pointer += 1
            if num == 0:
                nums[zero_pointer] = 0
                zero_pointer += 1
