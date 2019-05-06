from typing import List


class Solution:

    def maxArea(self, height: List[int]) -> int:
        area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            min_height = min(height[left], height[right])
            curr_area = min_height * (right - left)
            area = max(area, curr_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return area
