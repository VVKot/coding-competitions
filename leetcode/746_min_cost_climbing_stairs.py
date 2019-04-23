class Solution(object):

    def minCostClimbingStairs(self, cost):
        N = len(cost)
        prev_prev = cost[0]
        prev = cost[1]
        for i in range(2, N):
            curr = min(prev_prev, prev) + cost[i]
            prev_prev, prev = prev, curr
        return min(prev, prev_prev)
