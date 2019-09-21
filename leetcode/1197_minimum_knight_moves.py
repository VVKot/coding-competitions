class Solution:

    def minKnightMoves(self, x: int, y: int) -> int:
        moves = [(2, 1), (-2, 1), (2, -1), (-2, -1),
                 (1, 2), (1, -2), (-1, 2), (-1, -2)]
        x, y = abs(x), abs(y)
        stack = [(0, 0, 0)]
        distances = {(0, 0): 0}
        for r, c, d in stack:
            for dr, dc in moves:
                curr_r, curr_c = r+dr, c+dc
                if -2 <= curr_r <= x+2 and -2 <= curr_c <= y+2:
                    if (curr_r, curr_c) not in distances:
                        distances[(curr_r, curr_c)] = d+1
                        stack.append((curr_r, curr_c, d+1))
        return distances[(x, y)]
