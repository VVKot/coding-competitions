"""
T: O(N)
S: O(1) - additional

Just consider all possible cases - if remove interval does not touch
the current interval, if the start of the current interval should be
added to the result, and the same for the end of the interval.
"""


from typing import List


class Solution:

    def removeInterval(self,
                       intervals: List[List[int]],
                       toBeRemoved: List[int]) -> List[List[int]]:
        processed_intervals = []
        remove_start, remove_end = toBeRemoved
        for start, end in intervals:
            if start < remove_start:
                processed_intervals.append([start, min(end, remove_start)])
            if end > remove_end:
                processed_intervals.append([max(start, remove_end), end])
        return processed_intervals
