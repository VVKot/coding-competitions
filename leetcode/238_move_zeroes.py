from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        write, N = 0, len(nums)
        for num in nums:
            if num:
                nums[write] = num
                write += 1
        for i in range(write, N):
            nums[i] = 0
