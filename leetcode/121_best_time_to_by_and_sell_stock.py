from typing import List
from sys import maxsize as maxint


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_so_far = maxint
        for price in prices:
            min_so_far = min(min_so_far, price)
            max_profit = max(max_profit, price - min_so_far)
        return max_profit
