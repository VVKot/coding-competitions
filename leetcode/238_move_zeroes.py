from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        read, write, N = 0, 0, len(nums)
        while read < N:
            if nums[read]:
                nums[read], nums[write] = nums[write], nums[read]
                write += 1
            read += 1
