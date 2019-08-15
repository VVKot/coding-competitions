import operator
import functools
from typing import List


class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        zero_count = nums.count(0)
        if zero_count > 1:
            return [0] * N
        elif zero_count == 1:
            total = 1
            for num in nums:
                if num != 0:
                    total *= num
            return [total if num == 0 else 0 for num in nums]
        else:
            total = functools.reduce(operator.mul, nums)
            return [total//num for num in nums]
