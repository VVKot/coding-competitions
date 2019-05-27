from typing import List
from collections import Counter


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        result = 0
        for num, count in c.items():
            if k > 0 and num + k in c:
                result += 1
            if not k and count > 1:
                result += 1
        return result
