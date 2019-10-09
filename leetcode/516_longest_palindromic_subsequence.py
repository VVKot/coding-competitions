class Solution:

    def longestPalindromeSubseq(self, s: str) -> int:
        if s == s[::-1]:
            return len(s)
        N = len(s)
        dp = [[0] * (N+1) for _ in range(N+1)]
        for i in range(N+1):
            for j in range(N+1):
                if not i or not j:
                    dp[i][j] = 0
                elif s[i-1] == s[N-j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[N][N]
