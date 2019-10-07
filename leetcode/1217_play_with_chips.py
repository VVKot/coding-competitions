from typing import List


class Solution:

    def minCostToMoveChips(self, chips: List[int]) -> int:
        num_odds = sum(x % 2 for x in chips)
        return min(num_odds, len(chips) - num_odds)
