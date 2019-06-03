from typing import List


class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []  # type: List[List[int]]
        for start, end in sorted(intervals):
            if result and start <= result[-1][1]:
                result[-1][1] = max(result[-1][1], end)
            else:
                result.append([start, end])
        return result
