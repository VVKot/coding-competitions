from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zeroes = nums.count(0)
        nums[:] = [i for i in nums if i]
        nums += [0] * zeroes
