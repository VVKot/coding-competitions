class Solution:

    def help_rob(self, nums):
        prev_prev, prev = 0, 0
        for i in nums:
            prev_prev, prev = prev, max(prev_prev + i, prev)
        return prev

    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        without_last = self.help_rob(nums[:-1])
        without_first = self.help_rob(nums[1:])
        return max(without_last, without_first)
