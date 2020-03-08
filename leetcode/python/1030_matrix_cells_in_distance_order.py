class Solution:
    def allCellsDistOrder(self, R, C, r0, c0):
        cells = [[x, y] for x in range(R) for y in range(C)]
        cells = sorted(cells, key=lambda c: abs(c[0] - r0) + abs(c[1] - c0))
        return cells
