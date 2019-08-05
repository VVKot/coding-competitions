import collections
from typing import List


class Solution:

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []
        counts = collections.Counter(arr1)
        for num in arr2:
            result.extend([num] * counts[num])
            del counts[num]
        for num in sorted(counts.keys()):
            result.extend([num] * counts[num])
        return result
