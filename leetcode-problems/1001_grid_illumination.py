from collections import defaultdict


class Solution:
    def get_neighbors(self, y, x):
        return [(y, x), (y-1, x), (y+1, x), (y-1, x-1), (y+1, x+1), (y-1, x+1), (y+1, x-1), (y, x-1), (y, x+1)]

    def gridIllumination(self, N, lamps, queries):
        l_set = set()
        rows_on = defaultdict(int)
        cols_on = defaultdict(int)
        diag1_on = defaultdict(int)
        diag2_on = defaultdict(int)
        result = []
        for y, x in lamps:
            rows_on[y] += 1
            cols_on[x] += 1
            diag1_on[y-x] += 1
            diag2_on[y+x] += 1
            l_set.add((y, x))
        for y, x in queries:
            is_lit = rows_on[y] > 0 or cols_on[x] > 0 or diag1_on[y - x] > 0 or diag2_on[y+x] > 0
            result.append(1 if is_lit else 0)
            neighbors = self.get_neighbors(y, x)
            for r, c in neighbors:
                if (r, c) in l_set:
                    l_set.remove((r, c))
                    rows_on[r] -= 1
                    cols_on[c] -= 1
                    diag1_on[r-c] -= 1
                    diag2_on[r+c] -= 1
        return result
