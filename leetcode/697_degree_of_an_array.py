import collections
from typing import List


class Solution:

    def findShortestSubArray(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        max_count = counts.most_common(1)[0][1]
        sublists_len = []
        for val, count in counts.most_common():
            if count != max_count:
                break
            sublist_len = self.get_sublist_len(nums, val)
            sublists_len.append(sublist_len)
        return min(sublists_len)

    def get_sublist_len(self, nums: List[int], val: int) -> int:
        first, last = -1, -1
        for i, num in enumerate(nums):
            if num == val:
                if first == -1:
                    first = i
                last = i
        return last - first + 1
