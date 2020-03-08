from typing import List


class Solution:

    def insert(self,
               intervals: List[List[int]],
               newInterval: List[int]) -> List[List[int]]:
        l, r = newInterval
        before, after = [], []
        for start, end in intervals:
            if end < l:
                before.append([start, end])
            elif start > r:
                after.append([start, end])
            else:
                l = min(l, start)
                r = max(r, end)
        return before + [[l, r]] + after
