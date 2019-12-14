"""
T: O(logN)
S: O(logN)

The solution a is two-step process. First, we find the smallest number in the
list. After that, what's left is to do the binary search on the appropriate
half of the list
"""

from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        min_number_index = self.get_min_index(nums)
        if nums[min_number_index] <= target <= nums[-1]:
            return self.binary_search(nums, target, min_number_index,
                                      len(nums) - 1)
        else:
            return self.binary_search(nums, target, 0, min_number_index - 1)

    def get_min_index(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[0] <= nums[mid]:
                left = mid + 1
            else:
                right = mid
        return left

    def binary_search(self, nums: List[int], target: int, left: int,
                      right: int) -> int:
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
