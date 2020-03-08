class Solution:

    def new21Game(self, N: int, K: int, W: int) -> float:
        if K == 0 or N >= K + W:
            return 1.0
        dp = [0.0 for _ in range(N + 1)]
        dp[0] = 1.0
        wsum = 1.0
        for i in range(1, N + 1):
            dp[i] = wsum / W
            if i < K:
                wsum += dp[i]
            if i >= W:
                wsum -= dp[i - W]
        return sum(dp[K:])
