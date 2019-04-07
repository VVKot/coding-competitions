import operator
from functools import reduce


class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        return reduce(operator.xor, nums) ^ [n, 1, n+1, 0][n % 4]
