from typing import List


class Solution:

    def check_row(self, board: List[List[str]], i: int, j: int):
        val = board[i][j]
        for k in range(9):
            if k == i:
                continue
            if board[k][j] == val:
                return False
        return True

    def check_col(self, board: List[List[str]], i: int, j: int):
        val = board[i][j]
        for k in range(9):
            if k == j:
                continue
            if board[i][k] == val:
                return False
        return True

    def check_square(self, board: List[List[str]], i: int, j: int):
        val = board[i][j]
        row = i // 3
        col = j // 3
        for y in range(3*row, 3*(row+1)):
            for x in range(3*col, 3*(col+1)):
                if y == i and x == j:
                    continue
                if board[y][x] == val:
                    return False
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for y, row in enumerate(board):
            for x, ch in enumerate(row):
                if ch == '.':
                    continue
                valid = True
                valid &= self.check_row(board, y, x)
                valid &= self.check_col(board, y, x)
                valid &= self.check_square(board, y, x)
                if not valid:
                    return False
        return True
