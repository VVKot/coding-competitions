from typing import List


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        x2, y2 = points[1]
        x1, y1 = points[0]
        x3, y3 = points[2]
        return not ((y3 - y2)*(x2 - x1) == (y2 - y1)*(x3 - x2))
