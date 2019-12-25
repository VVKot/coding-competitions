"""
T: O(N)
S: O(N)

The result is bounded by two variables. Firstly, the kid can not get more than
half of all candy. Secondly, they can not get more kinds of candies that are
present. The minimum of those constraints is the answer.
"""

from typing import List


class Solution:

    def distributeCandies(self, candies: List[int]) -> int:
        candies_per_kid = len(candies) // 2
        candies_kind_count = len(set(candies))
        return min(candies_per_kid, candies_kind_count)
