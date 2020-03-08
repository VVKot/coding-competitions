class Solution:

    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)
        dp = list(range(l2+1))
        for i in range(1, l1+1):
            prev = i
            for j in range(1, l2+1):
                curr = 0
                if word1[i-1] == word2[j-1]:
                    curr = dp[j-1]
                else:
                    min_prev = min(prev, dp[j-1])
                    curr = min(min_prev, dp[j]) + 1
                dp[j-1] = prev
                prev = curr
            dp[l2] = prev
        return dp[l2]
