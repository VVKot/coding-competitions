from typing import List


class Solution:

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i, N = 0, len(nums)
        while i < N:
            while nums[i] != nums[nums[i]-1]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
            i += 1
        dissapeared_nums = []
        for i, num in enumerate(nums):
            if num != i+1:
                dissapeared_nums.append(i+1)
        return dissapeared_nums
