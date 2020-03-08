from typing import List


class Solution:

    SHIP, WATER = 'X', '.'

    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        for y, row in enumerate(board):
            for x, val in enumerate(row):
                if val == self.SHIP:
                    top = board[y-1][x] if y else self.WATER
                    left = board[y][x-1] if x else self.WATER
                    if left == top == self.WATER:
                        count += 1
        return count
