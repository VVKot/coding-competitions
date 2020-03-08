"""
T: O(N)
S: O(1)

Measure initial slope dy/dx. Check that the slope is the same for all
points. The regular way to do so is to check that dy/dx == dy_i/dx_i but that
can lead to division by zero. To avoid that we use multiplication form:
dx*dy_i == dx_i*dy
"""

from typing import List


class Solution:

    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x1, y1), (x2, y2) = coordinates[:2]
        dx = x2 - x1
        dy = y2 - y1
        return all(dx * (y - y2) == (x - x2) * dy for x, y in coordinates)
