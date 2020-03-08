from typing import List, Set, Tuple


class Solution:

    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not any(matrix):
            return []
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        pacific, atlantic = self.get_initial_oceans()
        self.expand_ocean(pacific)
        self.expand_ocean(atlantic)
        return list(map(list, pacific & atlantic))

    def get_initial_oceans(self) -> List[Set[Tuple[int, int]]]:
        pacific = set()
        atlantic = set()
        for y in range(self.rows):
            pacific.add((y, 0))
            atlantic.add((y, self.cols-1))
        for x in range(self.cols):
            pacific.add((0, x))
            atlantic.add((self.rows-1, x))
        return [pacific, atlantic]

    def expand_ocean(self, ocean: Set[Tuple[int, int]]) -> None:
        stack = list(ocean)
        while stack:
            y, x = stack.pop()
            for neighbor in self.get_higher_neighbors(y, x):
                if neighbor not in ocean:
                    ocean.add(neighbor)
                    stack.append(neighbor)

    def get_higher_neighbors(self, y, x) -> List[Tuple[int, int]]:
        lower_neighbors = []
        for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            curr_y, curr_x = y+dy, x+dx
            if 0 <= curr_y < self.rows and 0 <= curr_x < self.cols:
                if self.matrix[curr_y][curr_x] >= self.matrix[y][x]:
                    lower_neighbors.append((curr_y, curr_x))
        return lower_neighbors
