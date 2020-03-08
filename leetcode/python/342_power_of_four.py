class Solution:

    def isPowerOfFour(self, num):
        if num <= 0:
            return False
        if num & num-1:
            return False
        return not (num-1) % 3
