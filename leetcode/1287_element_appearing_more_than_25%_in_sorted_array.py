"""
T: O(logN)
S: O(1)

Given that the special integer occurs at least 25% of the time, it should be
present at one of these indices - N/4, N/2, 3N/4. We find the elements at these
indices, check their first and last occurrence, and if the count of them is
greater than 25% - return it.
"""

import bisect
from typing import List


class Solution:

    def findSpecialInteger(self, arr: List[int]) -> int:
        N = len(arr)
        quarter = N // 4
        if quarter == 0:
            return arr[0]
        for i in range(quarter, N, quarter):
            first_occurence = bisect.bisect_left(arr, arr[i])
            last_occurence = bisect.bisect_right(arr, arr[i])
            if last_occurence - first_occurence > quarter:
                return arr[i]
        return arr[0]
