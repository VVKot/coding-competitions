from typing import List, Dict


class Solution:

    def findShortestSubArray(self, nums: List[int]) -> int:
        counts = {}  # type: Dict[int, List[int]]
        for i, num in enumerate(nums):
            if num in counts:
                counts[num][0] += 1
                counts[num][2] = i
            else:
                counts[num] = [1, i, i]
        max_count = max(count for count, _, _ in counts.values())
        sublists_len = []
        for count, first, last in counts.values():
            if count == max_count:
                sublist_len = last - first + 1
                sublists_len.append(sublist_len)
        return min(sublists_len)
