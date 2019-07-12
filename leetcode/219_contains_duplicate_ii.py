from typing import List, Set


class Solution:

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()  # type: Set[int]
        for i, val in enumerate(nums):
            if i > k:
                seen.remove(nums[i - k - 1])
            if val in seen:
                return True
            else:
                seen.add(val)
        return False
