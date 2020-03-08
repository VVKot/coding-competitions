import math


class Solution:

    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:

        def lcm(a, b):
            return a * b // math.gcd(a, b)

        ab = lcm(a, b)
        bc = lcm(b, c)
        ac = lcm(a, c)
        abc = lcm(a, bc)
        lo, hi = 1, 2*(10**9)+1
        while lo < hi:
            mid = (lo+hi) // 2
            at_mid = mid//a + mid//b + mid//c - \
                mid//ab - mid//bc - mid//ac + mid//abc
            if at_mid < n:
                lo = mid+1
            else:
                hi = mid
        return lo
