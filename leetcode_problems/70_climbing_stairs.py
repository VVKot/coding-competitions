class Solution:
    def climbStairs(self, n):
        first = second = 1
        for _ in range(n):
            first, second = second, first + second
        return first
