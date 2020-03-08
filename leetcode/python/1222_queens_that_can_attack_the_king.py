from typing import List


class Solution:

    def queensAttacktheKing(self,
                            queens: List[List[int]],
                            king: List[int]) -> List[List[int]]:
        queens = set(tuple(q) for q in queens)
        attacking_queens = []
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                for k in range(1, 8):
                    curr_y, curr_x = king
                    curr_y += dy * k
                    curr_x += dx * k
                    if (curr_y, curr_x) in queens:
                        attacking_queens.append([curr_y, curr_x])
                        break
        return attacking_queens
