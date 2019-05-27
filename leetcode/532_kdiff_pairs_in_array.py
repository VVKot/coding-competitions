from typing import List, Set


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        result = set()
        nums.sort()
        comps = set()  # type: Set[int]
        for num in nums:
            if num - k in comps:
                result.add((num, num-k))
            comps.add(num)
        return len(result)
