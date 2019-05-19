import sys
from typing import List


class Solution:

    MINS_IN_HOUR = 60
    HOURS_IN_DAY = 24
    MINS_IN_DAY = HOURS_IN_DAY * MINS_IN_HOUR

    def get_mins(self, time: str) -> int:
        hours, mins = time.split(":")
        return int(hours) * self.MINS_IN_HOUR + int(mins)

    def findMinDifference(self, times: List[str]) -> int:
        all_mins = [0] * self.MINS_IN_DAY
        for time in times:
            mins = self.get_mins(time)
            all_mins[mins] += 1
        result = sys.maxsize
        prev, first = -1, -1
        for i in range(self.MINS_IN_DAY):
            num_of_times = all_mins[i]
            if num_of_times == 1:
                if prev == -1:
                    prev, first = i, i
                else:
                    result = min(result, i-prev)
                    prev = i
            elif num_of_times > 1:
                return 0
        over_midnight = self.MINS_IN_DAY - prev + first
        result = min(result, over_midnight)
        return result
