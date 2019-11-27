"""
T: O(N)
S: O(1)

For each position, we need to know the highest wall to the left
and to the right. The difference between the minimum of those and
the current bar's height is the amount of trapped water at the current
point. We utilize two points to continuously stay at the lower
end of the bars.
"""


from typing import List


class Solution:

    def trap(self, height: List[int]) -> int:
        trapped_volume = 0
        left, right = 0, len(height) - 1
        left_wall = right_wall = 0
        while left <= right:
            curr_left = height[left]
            curr_right = height[right]
            if curr_left <= curr_right:
                left_wall = max(left_wall, curr_left)
                trapped_volume += left_wall - curr_left
                left += 1
            else:
                right_wall = max(right_wall, curr_right)
                trapped_volume += right_wall - curr_right
                right -= 1
        return trapped_volume
