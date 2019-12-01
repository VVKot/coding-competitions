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
            if remove_end <= start or remove_start >= end:
                processed_intervals.append([start, end])
            else:
                if remove_start > start:
                    processed_intervals.append([start, remove_start])
                if remove_end < end:
                    processed_intervals.append([remove_end, end])
        return processed_intervals
