from typing import List
from operator import itemgetter


class Solution:

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        valid_count = 0
        last_end = float('-inf')
        for start, end in sorted(intervals, key=itemgetter(1)):
            if start >= last_end:
                valid_count += 1
                last_end = end
        return len(intervals) - valid_count
