class Solution:
    def minMoves2(self, nums):
        result = 0
        if not nums:
            return result
        nums = sorted(nums)
        mid = len(nums) // 2
        for n in nums:
            result += abs(n - nums[mid])
        return result
