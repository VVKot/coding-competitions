class Solution:

    def longestPalindromeSubseq(self, s: str) -> int:
        N = len(s)
        prev = [0] * (N+1)
        for i in range(N+1):
            curr = [0] * (N+1)
            for j in range(N+1):
                if not i or not j:
                    curr[j] = 0
                elif s[i-1] == s[N-j]:
                    curr[j] = prev[j-1] + 1
                else:
                    curr[j] = max(prev[j], curr[j-1])
            prev = curr[:]
        return curr[N]
