"""
T: O(NlogN)
S: O(N)

The straightforward solution - just sort timepoints and compare all adjacent
ones. The only trick that should be taken into account is the time interval
over midnight.
"""

from typing import List


class Solution:

    MINS_IN_HOUR = 60
    HOURS_IN_DAY = 24
    MINS_IN_DAY = HOURS_IN_DAY * MINS_IN_HOUR

    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        timestamps = self.get_timestamps(timePoints)
        min_difference = 24 * 60
        N = len(timestamps)
        for i in range(1, N):
            curr_difference = timestamps[i] - timestamps[i - 1]
            min_difference = min(min_difference, curr_difference)
        difference_over_midnight = \
            self.MINS_IN_DAY - timestamps[-1] + timestamps[0]
        min_difference = min(min_difference, difference_over_midnight)
        return min_difference

    def get_timestamps(self, timepoints: List[str]) -> List[int]:
        timestamps = []
        for timepoint in timepoints:
            hours, minutes = map(int, timepoint.split(":"))
            timestamps.append(hours * self.MINS_IN_HOUR + minutes)
        return timestamps
