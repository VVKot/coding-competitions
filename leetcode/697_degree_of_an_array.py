from typing import List, Dict


class Solution:

    def findShortestSubArray(self, nums: List[int]) -> int:
        counts = {}
        starts = {}  # type: Dict[int, int]
        result, max_count = 0, 0
        for i, num in enumerate(nums):
            if num not in starts:
                starts[num] = i
                counts[num] = 1
            else:
                counts[num] += 1
            sublist_len = i - starts[num] + 1
            curr_count = counts[num]
            if curr_count > max_count:
                max_count = curr_count
                result = sublist_len
            elif curr_count == max_count:
                result = min(result, sublist_len)
        return result
