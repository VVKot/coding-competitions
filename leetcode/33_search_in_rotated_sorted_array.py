"""
T: O(logN)
S: O(logN)

The one-pass solution to the problem. It can be done through observing the
invariances. We start the usual binary search, and if we found the appropriate
number we just return the index. Otherwise, there are two cases to consider:
1) nums[lo] <= nums[mid], part to the left of the mid is sorted, and if the
target can be in the sorted part, we go there, otherwise, we go right
2) otherwise the right part is sorted, and if the target is possibly in it,
we go right, otherwise, we go left
"""

from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return mid
            if nums[lo] <= nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[mid] < target <= nums[-1]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1
