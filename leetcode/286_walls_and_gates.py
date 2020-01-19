from typing import List, Tuple


class Solution:

    GATE, EMPTY = 0, 2147483647

    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        rooms_to_process = self.find_rooms_near_gates(rooms)
        curr_distance = 1
        while rooms_to_process:
            next_rooms_to_process = []
            for y, x in rooms_to_process:
                node = rooms[y][x]
                if node != self.EMPTY:
                    continue
                rooms[y][x] = curr_distance
                neighbors = self.get_neighbors(rooms, y, x)
                next_rooms_to_process.extend(neighbors)
            curr_distance += 1
            rooms_to_process = next_rooms_to_process

    def find_rooms_near_gates(self,
                              rooms: List[List[int]]) -> List[Tuple[int, int]]:
        rooms_near_gates = []
        for y, row in enumerate(rooms):
            for x, val in enumerate(row):
                if val != self.EMPTY:
                    continue
                for near_y, near_x in self.get_neighbors(rooms, y, x):
                    if rooms[near_y][near_x] == self.GATE:
                        rooms_near_gates.append((y, x))
                        break
        return rooms_near_gates

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
