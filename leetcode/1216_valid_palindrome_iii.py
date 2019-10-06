class Solution:

    def isValidPalindrome(self, s: str, k: int) -> bool:
        N = len(s)
        dp = [[0] * (N + 1) for _ in range(N + 1)]
        for i in range(N + 1):
            for j in range(N + 1):
                if not i or not j:
                    dp[i][j] = i or j
                elif s[i - 1] == s[N - j]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])
        return dp[N][N] <= k * 2
