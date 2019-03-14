class Solution:
    def solve(self, board):
        if not board or not len(board):
            return
        grid_y = len(board)
        grid_x = len(board[0])
        visited = set()
        for y in range(1, grid_y - 1):
            for x in range(1, grid_x - 1):
                if board[y][x] == "O" and (y, x) not in visited:
                    curr_visited = set()
                    stack = [(y, x)]
                    do_convert = True

                    while stack:
                        node_y, node_x = stack.pop()
                        if not self.is_inbound(grid_y, grid_x, node_y, node_x):
                            continue
                        curr_visited.add((node_y, node_x))
                        if self.is_border(grid_y, grid_x, node_y, node_x):
                            do_convert = False
                        adj_nodes = self.get_adj_nodes(node_y, node_x)
                        for r, c in adj_nodes:
                            if self.is_inbound(grid_y, grid_x, r, c) and board[r][c] == "O" and (r, c) not in curr_visited:
                                stack.append((r, c))

                    if do_convert:
                        for (yy, xx) in curr_visited:
                            board[yy][xx] = "X"
                    visited.union(curr_visited)

    def is_inbound(self, grid_y, grid_x, y, x):
        return y >= 0 and y < grid_y and x >= 0 and x < grid_x

    def is_border(self, grid_y, grid_x, y, x):
        return y == 0 or y == (grid_y - 1) or x == 0 or x == (grid_x-1)

    def get_adj_nodes(self, y, x):
        return [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]
