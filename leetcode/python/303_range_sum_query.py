class NumArray:

    def __init__(self, nums):
        N = len(nums)
        for i in range(1, N):
            nums[i] += nums[i-1]
        self.nums = nums

    def sumRange(self, i, j):
        left = self.nums[i-1] if i else 0
        right = self.nums[j]
        return right - left
