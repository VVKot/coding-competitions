class Solution:

    EPS = 0.00001

    def mySqrt(self, x):
        if x == 0 or x == 1:
            return x
        left, right = 0, x
        if x < 1:
            right = 1
        while left < right:
            mid = (left + right) / 2.0
            error = mid ** 2 - x
            if abs(error) < Solution.EPS:
                return int(mid)
            if error > 0:
                right = mid
            else:
                left = mid
        return -1

s = Solution()
s.mySqrt(5)