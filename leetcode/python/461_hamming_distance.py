class Solution:
    def hammingDistance(self, x, y):
        result = 0
        xor = x ^ y
        while xor:
            result += 1
            xor &= (xor-1)
        return result
