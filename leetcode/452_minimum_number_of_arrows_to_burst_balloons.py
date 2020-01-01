"""
T: O(NlogN)
S: O(1)

Greedily pop balloons from start to finish. For this to work properly sort
balloons by the end so that large balloon that spans over the next ones does
not impact the calculation.
"""

from typing import List


class Solution:

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x: x[1])
        arrows = 1
        prev_end = points[0][1]
        for start, end in points:
            if start > prev_end:
                arrows += 1
                prev_end = end
        return arrows
