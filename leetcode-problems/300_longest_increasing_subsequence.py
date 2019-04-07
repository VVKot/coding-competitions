import bisect

class Solution:
    def lengthOfLIS(self, nums):
        lis = [float('inf')] * (len(nums) + 1)
        for num in nums:
            lis[bisect.bisect_left(lis, num)] = num
        return lis.index(float('inf'))