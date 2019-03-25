from functools import reduce
import operator


class Solution:
    def singleNumber(self, nums):
        xor2 = reduce(operator.xor, nums)
        last_set_bit = xor2 & (-xor2)
        n1, n2 = 0, 0
        for num in nums:
            if num & last_set_bit:
                n1 ^= num
            else:
                n2 ^= num
        return [n1, n2]
