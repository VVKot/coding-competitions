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
        for interval in intervals:
            for reduced_interval in self.get_reduced_intervals(interval,
                                                               toBeRemoved):
                processed_intervals.append(reduced_interval)
        return processed_intervals

    def get_reduced_intervals(self,
                              interval: List[int],
                              to_remove: List[int]) -> List[List[int]]:
        start, end = interval
        remove_start, remove_end = to_remove
        if remove_end <= start or remove_start >= end:
            return [interval]
        reduced = []
        if remove_start > start:
            reduced.append([start, remove_start])
        if remove_end < end:
            reduced.append([remove_end, end])
        return reduced
