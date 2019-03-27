from functools import reduce
import operator

class Solution:
    def singleNumber(self, nums):
        return reduce(operator.xor, nums)
