import functools
import operator
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return functools.reduce(operator.xor, nums) ^ [n, 1, n+1, 0][n % 4]
