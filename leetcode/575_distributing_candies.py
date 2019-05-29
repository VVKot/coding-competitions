from typing import List


class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        half, diff = len(candies) // 2, len(set(candies))
        return min(half, diff)
