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
