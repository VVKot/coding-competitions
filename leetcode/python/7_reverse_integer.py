class Solution:
    def cmp(self, a, b):
        return (a>b) - (a<b)
    
    def reverse(self, x):
        sign = self.cmp(x, 0)
        result = int(repr(sign * x)[::-1])
        return sign*result * (result < 2**31)