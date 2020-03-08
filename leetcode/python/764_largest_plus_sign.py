from typing import List


class Solution:

    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        dp = [[0 for _ in range(N)] for j in range(N)]

        mines_set = {(a, b) for a, b in mines}
        result = 0
        for i in range(N):
            count = 0
            for j in range(N):
                curr = not (i, j) in mines_set
                count = count+1 if curr else 0
                dp[i][j] = count
            count = 0
            for j in range(N-1, -1, -1):
                curr = int(not (i, j) in mines_set)
                count = count+1 if curr else 0
                dp[i][j] = min(count, dp[i][j])

        for j in range(N):
            count = 0
            for i in range(N):
                curr = int(not (i, j) in mines_set)
                count = count+1 if curr else 0
                dp[i][j] = min(count, dp[i][j])
            count = 0
            for i in range(N-1, -1, -1):
                curr = int(not (i, j) in mines_set)
                count = count+1 if curr else 0
                dp[i][j] = min(count, dp[i][j])
                result = max(result, dp[i][j])
        return result
