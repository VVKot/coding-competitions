class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        if not nums or len(nums) < 2:
            return result
        nums = sorted(nums)
        for i in range(len(nums)-1):
            curr = nums[i+1] - nums[i]
            if curr > result:
                result = curr
        return result
