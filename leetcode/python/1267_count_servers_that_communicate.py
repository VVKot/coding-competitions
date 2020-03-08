"""
T: O(R*C)
S: O(R+C)

First, we count how many servers are at each row and column.
After that, for every server, we check whether there is another server
with which it is able to communicate.
"""


from typing import List


class Solution:

    def countServers(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        servers_at_row, servers_at_col = [0] * R, [0] * C
        for y, row in enumerate(grid):
            for x, val in enumerate(row):
                if val == 1:
                    servers_at_row[y] += 1
                    servers_at_col[x] += 1
        total = 0
        for y, row in enumerate(grid):
            for x, val in enumerate(row):
                if val == 1 and servers_at_row[y] + servers_at_col[x] > 2:
                    total += 1
        return total
