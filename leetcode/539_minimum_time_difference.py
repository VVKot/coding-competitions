from typing import List, Set


class Solution:

    MINS_IN_HOUR = 60
    HOURS_IN_DAY = 24
    MINS_IN_DAY = HOURS_IN_DAY * MINS_IN_HOUR

    def findMinDifference(self, times: List[str]) -> int:
        timestamps_as_minutes = set()  # type: Set[int]
        for timestamp in times:
            mins = self.get_mins(timestamp)
            if mins in timestamps_as_minutes:
                return 0
            timestamps_as_minutes.add(mins)
        result = self.MINS_IN_DAY
        prev, first = -1, -1
        for time in range(self.MINS_IN_DAY):
            if time not in timestamps_as_minutes:
                continue
            if prev == -1:
                prev = first = time
            else:
                result = min(result, time-prev)
                prev = time
        over_midnight = self.MINS_IN_DAY - prev + first
        result = min(result, over_midnight)
        return result

    def get_mins(self, timestamp: str) -> int:
        hours, mins = map(int, timestamp.split(":"))
        return hours * self.MINS_IN_HOUR + mins
