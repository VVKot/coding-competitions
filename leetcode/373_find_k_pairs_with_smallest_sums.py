from typing import List


class Solution:

    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        result = [[a, b] for a in nums1 for b in nums2]
        result.sort(key=lambda x: x[0]+x[1])
        return result[:k]
