from typing import List


class Solution:

    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        N = len(intervals)
        for i in range(1, N):
            _, prev_end = intervals[i-1]
            curr_start, _ = intervals[i]
            if curr_start < prev_end:
                return False
        return True
