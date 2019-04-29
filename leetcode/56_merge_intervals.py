from typing import List


class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []  # type: List[List[int]]
        intervals.sort()
        for start, end in intervals:
            if not merged:
                merged.append([start, end])
            prev_end = merged[-1][1]
            if prev_end < start:
                merged.append([start, end])
            else:
                merged[-1][1] = max(prev_end, end)
        return merged
