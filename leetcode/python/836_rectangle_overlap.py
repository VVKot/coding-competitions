from typing import List


class Solution:

    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        ax_min, ay_min, ax_max, ay_max = rec1
        bx_min, by_min, bx_max, by_max = rec2
        right = min(ax_max, bx_max)
        left = max(ax_min, bx_min)
        if not right > left:
            return False
        bottom = max(ay_min, by_min)
        top = min(ay_max, by_max)
        if not top > bottom:
            return False
        return True
