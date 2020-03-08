class Solution:
    def canJump(self, nums):
        max_ = 0
        for curr, num in enumerate(nums):
            if curr > max_:
                return False
            max_ = max(max_, curr+num)
        return True