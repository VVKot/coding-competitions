class Solution:
    def hammingDistance(self, x, y):
        result = 0
        while x or y:
            if (x & 1) ^ (y & 1):
                result += 1
            x = x >> 1
            y = y >> 1
        return result