from typing import List


class Solution:

    DEAD, ALIVE, BECAME_DEAD, BECAME_ALIVE = range(4)

    def gameOfLife(self, board: List[List[int]]) -> None:
        self.determine_new_state(board)
        self.unify_states(board)

    def determine_new_state(self, board: List[List[int]]) -> None:
        for y, row in enumerate(board):
            for x, val in enumerate(row):
                alive_neighbors = self.get_alive(board, y, x)
                state = self.DEAD
                if val == self.ALIVE:
                    if alive_neighbors in (2, 3):
                        state = self.ALIVE
                    else:
                        state = self.BECAME_DEAD
                else:
                    if alive_neighbors == 3:
                        state = self.BECAME_ALIVE
                board[y][x] = state

    def unify_states(self, board: List[List[int]]) -> None:
        for y, row in enumerate(board):
            for x, val in enumerate(row):
                if val == self.BECAME_ALIVE:
                    board[y][x] = self.ALIVE
                if val == self.BECAME_DEAD:
                    board[y][x] = self.DEAD

    def get_alive(self, board: List[List[int]], y: int, x: int) -> int:
        neighbors = [(y-1, x-1), (y-1, x), (y-1, x+1), (y, x-1),
                     (y, x+1), (y+1, x-1), (y+1, x), (y+1, x+1)]
        alive = 0
        for curr_y, curr_x in neighbors:
            if self.is_valid(board, curr_y, curr_x):
                alive += board[curr_y][curr_x] in (self.ALIVE,
                                                   self.BECAME_DEAD)
        return alive

    def is_valid(self, board: List[List[int]], y: int, x: int) -> bool:
        rows, cols = len(board), len(board[0])
        return 0 <= y < rows and 0 <= x < cols
