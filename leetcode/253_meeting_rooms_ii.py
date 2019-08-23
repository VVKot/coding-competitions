import heapq
from typing import List


class Solution:

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort()
        meeting_ends = []  # type: List[int]
        for start, end in intervals:
            if meeting_ends and meeting_ends[0] <= start:
                heapq.heappop(meeting_ends)
            heapq.heappush(meeting_ends, end)
        return len(meeting_ends)
