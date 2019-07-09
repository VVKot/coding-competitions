import functools
import operator
from typing import List


class Solution:

    def findErrorNums(self, nums: List[int]) -> List[int]:
        N = len(nums)
        total = functools.reduce(operator.xor, nums)
        total = functools.reduce(operator.xor, range(1, N+1), total)
        rightmost_set = total & ~(total - 1)
        xor1 = xor2 = 0
        for num in nums:
            if num & rightmost_set:
                xor1 ^= num
            else:
                xor2 ^= num
        for num in range(1, N+1):
            if num & rightmost_set:
                xor1 ^= num
            else:
                xor2 ^= num
        for num in nums:
            if num == xor1:
                return [xor1, xor2]
        return [xor2, xor1]
