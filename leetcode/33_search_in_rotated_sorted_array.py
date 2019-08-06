from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        max_index = self.get_pivot(nums, target)
        if nums[0] <= target <= nums[max_index]:
            return self.binary_search(nums, 0, max_index, target)
        else:
            return self.binary_search(nums, max_index+1, len(nums)-1, target)

    def get_pivot(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left != right:
            mid = (left+right) // 2
            if nums[mid] > nums[left]:
                left = mid
            else:
                right = mid
        return left

    def binary_search(self,
                      nums: List[int],
                      left: int,
                      right: int,
                      target: int) -> int:
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
