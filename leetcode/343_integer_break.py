class Solution:

    def integerBreak(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[1] = 1
        for i in range(2, n+1):
            for j in range(1, i):
                max_prev_product = max(dp[i-j], i-j)
                dp[i] = max(dp[i], max_prev_product * j)
        return dp[n]
