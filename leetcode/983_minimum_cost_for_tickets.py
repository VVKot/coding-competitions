from sys import maxsize as maxint
from typing import List


class Solution:

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        N = len(days)
        dp = [0] + [maxint] * N
        for i in range(N):
            for cost, ticket_duration in zip(costs, (1, 7, 30)):
                new_cost = dp[i] + cost
                j = i
                while j < N and days[j] - days[i] < ticket_duration:
                    dp[j+1] = min(dp[j+1], new_cost)
                    j += 1
        return dp[N]
