import functools
import operator
from typing import List


class Solution:

    def singleNumber(self, nums: List[int]) -> List[int]:
        diff = functools.reduce(operator.xor, nums)
        diff &= -diff
        result = [0, 0]
        for num in nums:
            if num & diff:
                result[0] ^= num
            else:
                result[1] ^= num
        return result
