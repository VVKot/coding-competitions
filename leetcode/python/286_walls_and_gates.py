import collections
from typing import List, Tuple


class Solution:

    GATE, EMPTY = 0, 2147483647

    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        rooms_to_process = collections.deque(self.find_gates(rooms))
        while rooms_to_process:
            y, x = rooms_to_process.popleft()
            for near_y, near_x in self.get_neighbors(rooms, y, x):
                if rooms[near_y][near_x] != self.EMPTY:
                    continue
                rooms_to_process.append((near_y, near_x))
                rooms[near_y][near_x] = rooms[y][x] + 1

    def find_gates(self, rooms: List[List[int]]) -> List[Tuple[int, int]]:
        gates = []
        for y, row in enumerate(rooms):
            for x, val in enumerate(row):
                if val == self.GATE:
                    gates.append((y, x))
        return gates

    def get_neighbors(self, rooms: List[List[int]], y: int,
                      x: int) -> List[Tuple[int, int]]:
        rows = len(rooms)
        cols = len(rooms[0])
        neighbors = []
        for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            curr_y, curr_x = y + dy, x + dx
            if 0 <= curr_y < rows and 0 <= curr_x < cols:
                neighbors.append((curr_y, curr_x))
        return neighbors
