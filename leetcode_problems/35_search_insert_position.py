class Solution:
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            mid_value = nums[mid]
            if mid_value >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left
