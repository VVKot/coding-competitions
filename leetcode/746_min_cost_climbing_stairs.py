from typing import List


class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        for i in range(2, N):
            cost[i] = min(cost[i-1], cost[i-2]) + cost[i]
        return min(cost[N-1], cost[N-2])
