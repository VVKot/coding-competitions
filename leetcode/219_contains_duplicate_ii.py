from typing import List, Dict


class Solution:

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_seen = {}  # type: Dict[int, int]
        for i, val in enumerate(nums):
            if val in last_seen and i - last_seen[val] <= k:
                return True
            last_seen[val] = i
        return False
