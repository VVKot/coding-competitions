from typing import List


class Solution:

    OFFSET = 10
    DEAD, ALIVE = range(2)

    def gameOfLife(self, board: List[List[int]]) -> None:
        self.count_neighbors(board)
        self.get_next_generation(board)

    def count_neighbors(self, board: List[List[int]]) -> None:
        for y, row in enumerate(board):
            for x, val in enumerate(row):
                alive = self.get_alive(board, y, x)
                if val == self.ALIVE:
                    alive += self.OFFSET
                board[y][x] = alive

    def get_next_generation(self, board: List[List[int]]) -> None:
        for y, row in enumerate(board):
            for x, val in enumerate(row):
                state = self.DEAD
                if val >= self.OFFSET:
                    val -= self.OFFSET
                    if val in (2, 3):
                        state = self.ALIVE
                else:
                    if val == 3:
                        state = self.ALIVE
                board[y][x] = state

    def get_alive(self, board: List[List[int]], y: int, x: int) -> int:
        alive = 0
        for curr_y, curr_x in [(y-1, x-1), (y-1, x), (y-1, x+1), (y, x-1)]:
            if self.is_valid(board, curr_y, curr_x):
                alive += board[curr_y][curr_x] >= self.OFFSET
        for curr_y, curr_x in [(y, x+1), (y+1, x-1), (y+1, x), (y+1, x+1)]:
            if self.is_valid(board, curr_y, curr_x):
                alive += board[curr_y][curr_x] == self.ALIVE
        return alive

    def is_valid(self, board: List[List[int]], y: int, x: int) -> bool:
        rows, cols = len(board), len(board[0])
        return 0 <= y < rows and 0 <= x < cols
