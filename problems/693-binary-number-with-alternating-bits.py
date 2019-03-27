class Solution:
    def hasAlternatingBits(self, n):
        if not n:
            return False
        num = n ^ (n >> 1)
        return not (num & (num + 1))
