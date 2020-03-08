from typing import List


class Solution:

    def singleNumber(self, nums: List[int]) -> int:
        ones, twos, n = 0, -1, len(nums)
        for i in range(n):
            ones = ones ^ nums[i] & twos
            twos = twos ^ nums[i] & ones
        return ones
