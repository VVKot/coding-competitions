class Solution:
    def minMoves2(self, nums):
        nums = sorted(nums)
        return sum(abs(nums[len(nums) // 2] - i) for i in nums)
