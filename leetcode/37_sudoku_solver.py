from typing import List, Tuple


class Solution:

    def is_valid(self, row: int, col: int, ch: str) -> bool:
        boxrow = row - row % 3
        boxcol = col - col % 3
        if self.checkrow(row, ch) \
                and self.checkcol(col, ch) \
                and self.checksquare(boxrow, boxcol, ch):
            return True
        return False

    def checkrow(self, row: int, ch: str) -> bool:
        for col in range(9):
            if self.board[row][col] == ch:
                return False
        return True

    def checkcol(self, col, ch) -> bool:
        for row in range(9):
            if self.board[row][col] == ch:
                return False
        return True

    def checksquare(self, row: int, col: int, ch: str) -> bool:
        for r in range(row, row+3):
            for c in range(col, col+3):
                if self.board[r][c] == ch:
                    return False
        return True

    def solveSudoku(self, board: List[List[str]]):
        self.board = board
        self.solve()

    def findUnassigned(self) -> Tuple[int, int]:
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == ".":
                    return row, col
        return -1, -1

    def solve(self) -> bool:
        row, col = self.findUnassigned()
        if row == -1 and col == -1:
            return True
        for num in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.solve():
                    return True
                self.board[row][col] = "."
        return False
