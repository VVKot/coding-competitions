from typing import List


class DSU:

    def __init__(self, N: int):
        self.parents = list(range(N))
        self.ranks = [0] * N

    def find(self, node: int) -> int:
        if self.parents[node] == node:
            return node
        self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

    def union(self, n1: int, n2: int) -> None:
        p1, p2 = map(self.find, (n1, n2))
        rank1, rank2 = map(self.ranks.__getitem__, (p1, p2))
        if rank1 >= rank2:
            if rank1 == rank2:
                rank1 += 1
            self.parents[p2] = p1
        else:
            self.parents[p1] = p2


class Solution:

    def regionsBySlashes(self, grid: List[str]) -> int:
        N = len(grid)
        subsquare_count = N*N*4
        dsu = DSU(subsquare_count)
        rows = len(grid)
        cols = len(grid[0])
        for y, row in enumerate(grid):
            for x, val in enumerate(row):
                curr_top = 4 * (y*N + x)
                curr_left = curr_top + 1
                curr_right = curr_top + 2
                curr_bottom = curr_top + 3
                if val in '/ ':
                    dsu.union(curr_top, curr_left)
                    dsu.union(curr_right, curr_bottom)
                if val in '\ ':
                    dsu.union(curr_top, curr_right)
                    dsu.union(curr_left, curr_bottom)

                if y > 0:
                    bottom_of_the_top_node = (curr_top - 4*N) + 3
                    dsu.union(curr_top, bottom_of_the_top_node)
                if y < rows-1:
                    top_of_the_bottom_node = (curr_top + 4*N)
                    dsu.union(curr_bottom, top_of_the_bottom_node)
                if x > 0:
                    right_of_the_left_node = (curr_top - 4) + 2
                    dsu.union(curr_left, right_of_the_left_node)
                if x < cols-1:
                    left_of_the_right_node = (curr_top + 4) + 1
                    dsu.union(curr_right, left_of_the_right_node)

        return sum(dsu.find(node) == node for node in range(subsquare_count))
