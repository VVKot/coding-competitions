class Solution(object):

    def singleNumber(self, nums):
        ones, twos , n = 0, -1, len(nums)
        for i in range(n):
            ones = ones ^ nums[i] & twos
            twos = twos ^ nums[i] & ones
        return ones

s = Solution()
s.singleNumber([1,2,1,1])