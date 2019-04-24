class Solution:

    def mySqrt(self, x):
        if not x:
            return x
        r = x
        while r*r > x:
            r = (r + x//r) // 2
        return int(r)
