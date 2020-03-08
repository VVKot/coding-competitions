from typing import List


class Solution:

    def maxArea(self, height: List[int]) -> int:
        area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            left_bar = height[left]
            right_bar = height[right]
            height = min(left_bar, right_bar)
            width = right - left
            area = max(area, height*width)
            if left_bar < right_bar:
                left += 1
            else:
                right -= 1
        return area
