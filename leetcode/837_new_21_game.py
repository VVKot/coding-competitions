class Solution:

    def new21Game(self, N: int, K: int, W: int) -> float:
        if K == 0 or N > K + W:
            return 1.0
        dp = [0.0 for _ in range(K + W)]
        dp[0] = 1.0
        for i in range(1, K + W):
            dp[i] = dp[i - 1]
            if i <= W:
                dp[i] += dp[i - 1] / W
            else:
                dp[i] += (dp[i - 1] - dp[i - W - 1]) / W
            if i > K:
                dp[i] -= (dp[i - 1] - dp[K - 1]) / W
        return dp[N] - dp[K - 1]
