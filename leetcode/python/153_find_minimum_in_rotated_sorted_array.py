"""
T: O(logN)
S: O(1)

A classic binary search problem. Only conditions are changed a bit.
1) If the current element is greater than the right boundary, we should go to
the right. That is because when this condition holds, the pivot element is in
between the current element and the right boundary.
2) Otherwise, we can conclude that the part of the array between the current
and the right is sorted, so we want to go to the left. We should be careful to
not exclude mid in this case, since it is might be the answer.
"""

from typing import List


class Solution:

    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left != right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[right]
