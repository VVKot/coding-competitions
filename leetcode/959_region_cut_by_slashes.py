from typing import List


class Solution:

    def regionsBySlashes(self, grid: List[str]) -> int:
        self.grid = grid
        parents = self.get_node_parents()

        def find(node):
            if parents[node] == node:
                return node
            else:
                return find(parents[node])

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            parents[p1] = p2  # TODO - add union by rank

        for y, row in enumerate(grid):
            for x, val in enumerate(row):
                first = second = None
                if val == ' ':
                    first, second = self.get_regions(y, x)
                elif val == '/':
                    first, _ = self.get_regions(y, x)
                    second = first
                else:
                    first, second = self.get_regions(y, x)
                if x != 0:
                    left = self.get_left(y, x)
                    union(first, left)
                if y != 0:
                    top = self.get_top(y, x)
                    union(second, top)
        return len(set(find(p) for p in parents))

    def get_regions(self, y, x):
        first_mark, second_mark = 0, 1
        val = self.grid[y][x]
        if val == ' ':
            return (y, x, first_mark), (y, x, first_mark)
        else:
            return (y, x, first_mark), (y, x, second_mark)

    def get_left(self, y, x):
        val = self.grid[y][x-1]
        if val == ' ':
            return self.get_regions(y, x-1)[0]
        else:
            return self.get_regions(y, x-1)[1]

    def get_top(self, y, x):
        val = self.grid[y-1][x]
        if val == ' ':
            return self.get_regions(y-1, x)[0]
        elif val == '/':
            return self.get_regions(y-1, x)[1]
        else:
            return self.get_regions(y-1, x)[0]

    def get_node_parents(self):
        parents = {}
        for y, row in enumerate(self.grid):
            for x, val in enumerate(row):
                first, second = self.get_regions(y, x)
                parents[first] = first
                parents[second] = second
        return parents
