class Solution:

    def hammingWeight(self, n):
        result = 0
        while n:
            result += 1
            n &= n - 1
        return result
