from typing import List


class Solution:

    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        N = len(nums)
        result = [-1] * N
        nums_to_process = []  # type: List[int]
        for i, num in enumerate(nums):
            while nums_to_process and nums[nums_to_process[-1]] < num:
                result[nums_to_process.pop()] = num
            nums_to_process.append(i)
        for num in nums:
            if not nums_to_process:
                break
            while nums_to_process and nums[nums_to_process[-1]] < num:
                result[nums_to_process.pop()] = num
        return result
