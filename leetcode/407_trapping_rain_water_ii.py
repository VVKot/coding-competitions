import heapq
from sys import maxsize
from typing import List, Tuple


class Solution:

    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.height_map = []
        self.visited_map = []

    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not any(heightMap):
            return 0
        self.setup_maps(heightMap)
        return self.get_trapped_volume()

    def setup_maps(self, height_map: List[List[int]]) -> None:
        self.rows = len(height_map)
        self.cols = len(height_map[0])
        self.height_map = height_map
        self.visited_map = [[False for _ in range(self.cols)]
                            for _ in range(self.rows)]

    def get_trapped_volume(self) -> int:
        volume = 0
        max_height = -maxsize
        points_queue = self.get_points_queue()
        while points_queue:
            height, y, x = heapq.heappop(points_queue)
            self.visited_map[y][x] = True
            max_height = max(max_height, height)
            if height < max_height:
                volume += max_height - height
            near = self.get_near(y, x)
            for near_y, near_x in near:
                if not self.visited_map[near_y][near_x]:
                    self.visited_map[near_y][near_x] = True
                    near_height = self.height_map[near_y][near_x]
                    heapq.heappush(points_queue, (near_height, near_y, near_x))
        return volume

    def get_points_queue(self) -> List[Tuple[int, int, int]]:
        points_queue = []  # type: List[Tuple[int, int, int]]
        borders = self.get_borders(self.rows, self.cols)
        for y, x in borders:
            heapq.heappush(points_queue, (self.height_map[y][x], y, x))
        return points_queue

    def get_borders(self, rows: int, cols: int) -> List[Tuple[int, int]]:
        borders = []
        for x in range(cols):
            borders.append((0, x))
            borders.append((rows-1, x))
        for y in range(1, rows-1):
            borders.append((y, 0))
            borders.append((y, cols-1))
        return borders

    def get_near(self, y: int, x: int) -> List[Tuple[int, int]]:
        near = []
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            curr_y, curr_x = y+dy, x+dx
            if 0 <= curr_y < self.rows and 0 <= curr_x < self.cols:
                near.append((curr_y, curr_x))
        return near
