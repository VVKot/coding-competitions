from sys import maxsize as maxint
from typing import List


class Solution:

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        N = len(days)
        dp = [maxint] * N + [0]
        for i in reversed(range(N)):
            for cost, ticket_duration in zip(costs, (1, 7, 30)):
                j = i
                while j < N and days[j] - days[i] < ticket_duration:
                    j += 1
                dp[i] = min(dp[i], dp[j] + cost)
        return dp[0]
