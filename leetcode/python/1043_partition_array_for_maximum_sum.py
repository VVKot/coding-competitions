from typing import List


class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        N = len(A)
        dp = [0] * N
        for i in range(N):
            j, left = i, max(0, i - K + 1)
            curr_max = 0
            while j >= left:
                curr_max = max(curr_max, A[j])
                count = i - j + 1
                prev = dp[j - 1] if j else 0
                dp[i] = max(dp[i], prev + count * curr_max)
                j -= 1
        return dp[N - 1]
