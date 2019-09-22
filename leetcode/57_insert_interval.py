from typing import List


class Solution:

    def insert(self,
               intervals: List[List[int]],
               newInterval: List[int]) -> List[List[int]]:
        result = []  # type: List[List[int]]

        def merge(start, end):
            if result and result[-1][1] >= start:
                result[-1][1] = max(end, result[-1][1])
            else:
                result.append([start, end])

        l, r = newInterval
        interval_merged = False
        for i, j in intervals:
            if not interval_merged and i > l:
                interval_merged = True
                merge(l, r)
            merge(i, j)
        if not interval_merged:
            merge(l, r)
        return result
