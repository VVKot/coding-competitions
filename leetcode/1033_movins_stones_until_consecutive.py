"""
T: O(1)
S: O(1)

The maximum number of moves is just the total number of empty slots between
stones. The minimum number is:
* 0 - if there are no empty slots, i.e. both gaps have length 0
* 1 - if one of the gaps is of length 0 or 1
* 2 - if neither of the mentioned conditions is satisfied
"""

from typing import List


class Solution:

    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a, b, c = sorted([a, b, c])
        left_gap = abs(b - a) - 1
        right_gap = abs(c - b) - 1
        max_moves = left_gap + right_gap
        min_moves = 1
        if left_gap == right_gap == 0:
            min_moves = 0
        elif left_gap > 1 and right_gap > 1:
            min_moves = 2
        return [min_moves, max_moves]
