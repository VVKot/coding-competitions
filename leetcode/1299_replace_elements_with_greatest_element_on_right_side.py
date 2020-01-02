"""
T: O(N)
S: O(1)

Iterate from the back, remember the max element to right, reassign the current
element before updating the max.
"""

from typing import List


class Solution:

    def replaceElements(self, arr: List[int]) -> List[int]:
        max_right, N = -1, len(arr)
        for i in reversed(range(N)):
            arr[i], max_right = max_right, max(max_right, arr[i])
        return arr
