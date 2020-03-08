from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        N = len(prices)
        for i in range(1, N):
            possible_profit = prices[i] - prices[i-1]
            if possible_profit > 0:
                profit += possible_profit
        return profit
