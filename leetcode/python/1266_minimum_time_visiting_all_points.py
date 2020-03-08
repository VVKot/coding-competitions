"""
T: O(N)
S: O(1)

Time to travel between two points is the maximum of their coordinate
differences. Firstly, we can move diagonally, and cover MIN(D1, D2) distance.
After that, we start moving horizontally or vertically for ABS(D1, D2) units.
Combining these two measurements gives as MAX(D1, D2).
"""


from typing import List


class Solution:

    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total = 0
        N = len(points)
        for i in range(1, N):
            y1, x1 = points[i-1]
            y2, x2 = points[i]
            d1, d2 = abs(y1-y2), abs(x1-x2)
            total += max(d1, d2)
        return total
