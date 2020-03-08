class Solution:
    def findMaximumXOR(self, nums):
        result = 0
        for i in range(31, -1, -1):
            result <<= 1
            prefixes = {num >> i for num in nums}
            result += any(result^1 ^ pref in prefixes for pref in prefixes)
        return result