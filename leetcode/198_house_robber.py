class Solution:

    def rob(self, nums):
        prev_prev, prev = 0, 0
        for i in nums:
            prev_prev, prev = prev, max(prev_prev + i, prev)
        return prev
