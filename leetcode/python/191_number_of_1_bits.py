class Solution:

    def hammingWeight(self, n):
        bit_count = 0
        while n:
            bit_count += 1
            n &= n - 1
        return bit_count
